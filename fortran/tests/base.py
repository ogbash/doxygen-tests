
import unittest
import libxml2
import os.path

class TestException (Exception):
    pass

class FortranTestCase(unittest.TestCase):

    def __init__(self, name):
        unittest.TestCase.__init__(self, name)
        self.docs = {}
        self.path = "xml"

    def getDoc(self, filename):
        "Get XML document for the file."
        if self.docs.has_key(filename):
            return self.docs[filename]
        try:
            doc = libxml2.parseFile(os.path.join(self.path,filename))
        except Exception, e:
            raise TestException("XML parse of file '%s' failed: %s",filename, str(e))
        self.docs[filename] = doc
        return doc

    def getFileDoc(self, name):
        "Get XML document for Fortran file."

        parts = name.split(".")
        basename = ".".join(parts[:-1])
        ext = parts[-1]
        filename = "%s_8%s.xml" % (basename, ext)
        return self.getDoc(filename)

    def getModuleDoc(self, name):
        "Get XML document for Fortran module."

        name = name.replace("_", "__") # doxygen doubles underscores (?)
        filename = "namespace%s.xml" % name
        return self.getDoc(filename)
    
    def getModule(self, name):
        "Get Fortran module XML element from its document."
        doc = self.getModuleDoc(name)
        modules = doc.xpathEval("doxygen/compounddef[@kind='namespace'][compoundname='%s']"%name)
        self.assertEqual(len(modules),1)
        return modules[0]

    def getFile(self, name):
        "Get Fortran file XML element from its document."

        doc = self.getFileDoc(name)
        files = doc.xpathEval("doxygen/compounddef[@kind='file'][compoundname='%s']"%name)
        self.assertEqual(len(files),1)
        return files[0]

    def getSubprogram(self, compound, subprogramName):
        "Find subprogram XML element in module or file element."

        subprograms = compound.xpathEval("sectiondef[@kind='func']/memberdef[@kind='function'][name='%s']"%subprogramName)
        self.assertEqual(len(subprograms),1)
        return subprograms[0]

    def getSubprogramPublic(self, compound, subprogramName):
        "Find subprogram XML element in public-func section of the interface."

        subprograms = compound.xpathEval("sectiondef[@kind='public-func']/memberdef[@kind='function'][name='%s']"%subprogramName)
        self.assertEqual(len(subprograms),1)
        return subprograms[0]

    def getParamDescription(self, subprogram, paramName):
        "Get parameter description element in subprogram element."

        desc = subprogram.xpathEval("param[defname='%s']/briefdescription"%paramName)
        self.assertEqual(len(desc),1)
        return desc[0]

    def getModuleVariable(self, module, varName):
        "Get variable entity."
        var = module.xpathEval("sectiondef[@kind='var']/memberdef[@kind='variable'][name='%s']"%varName)
        return var[0]

    def getVarDescription(self, module, varName):
        "Get variable description entity in module."
        var = self.getModuleVariable(module, varName)
        desc = var.xpathEval("briefdescription")
        self.assertEqual(len(desc),1)
        return desc[0]

    def getInnerInterface(self,  module, intfName):
        "Get Fortran interface."

        moduleName = module.xpathEval("compoundname")[0].getContent()
        intfNameFull = "%s::%s" % (moduleName,intfName)
        intfRef = module.xpathEval("*[self::innerclass='%s']" % intfNameFull)[0]
        refid = intfRef.prop('refid')
        intfDoc = self.getDoc("%s.xml" % refid)
        intf = intfDoc.xpathEval("doxygen/compounddef[@id='%s'][compoundname='%s']" % 
                                 (refid,intfNameFull))
        return intf[0]

