
import unittest
import libxml2
import os.path

class FortranTestCase(unittest.TestCase):

    def __init__(self, name):
        unittest.TestCase.__init__(self, name)
        self.docs = {}
        self.path = "xml"

    def getDoc(self, filename):
        if self.docs.has_key(filename):
            return self.docs[filename]
        doc = libxml2.parseFile(os.path.join(self.path,filename))
        self.docs[filename] = doc
        return doc

    def getFileDoc(self, name):
        parts = name.split(".")
        basename = ".".join(parts[:-1])
        ext = parts[-1]
        filename = "%s_8%s.xml" % (basename, ext)
        return self.getDoc(filename)

    def getModuleDoc(self, name):
        filename = "namespace%s.xml" % name
        return self.getDoc(filename)
    
    def getModule(self, name):
        doc = self.getModuleDoc(name)
        modules = doc.xpathEval("doxygen/compounddef[@kind='namespace'][compoundname='%s']"%name)
        self.assertEqual(len(modules),1)
        return modules[0]

    def getFile(self, name):
        doc = self.getFileDoc(name)
        files = doc.xpathEval("doxygen/compounddef[@kind='file'][compoundname='%s']"%name)
        self.assertEqual(len(files),1)
        return files[0]

    def getSubprogram(self, compound, subprogramName):
        "Find subprogram in module or file."
        subprograms = compound.xpathEval("sectiondef[@kind='func']/memberdef[@kind='function'][name='%s']"%subprogramName)
        self.assertEqual(len(subprograms),1)
        return subprograms[0]

    def getParamDescription(self, subprogram, paramName):
        desc = subprogram.xpathEval("param[defname='%s']/briefdescription"%paramName)
        self.assertEqual(len(desc),1)
        return desc[0]

    def getModuleVariable(self, module, varName):
        var = module.xpathEval("sectiondef[@kind='var']/memberdef[@kind='variable'][name='%s']"%varName)
        return var[0]

    def getVarDescription(self, module, varName):
        var = self.getModuleVariable(module, varName)
        desc = var.xpathEval("briefdescription")
        self.assertEqual(len(desc),1)
        return desc[0]
