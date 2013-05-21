import logging
LOG = logging.getLogger(__name__)

import unittest
import libxml2
import os.path
import tempfile
import shutil
import subprocess

config = dict()

class TestException (Exception):
    pass

class FortranTestCase(unittest.TestCase):
    BASEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    TESTSPATH = os.path.join(BASEPATH,"tests","fortran")
    FILES = []

    def __init__(self, name):
        unittest.TestCase.__init__(self, name)
        self.docs = {}
        self.path = "xml"

    def setUp(self):
        # create work directory
        self.wrkdir = config.get('outdir',tempfile.mkdtemp(prefix="doxytest"))
        if not os.path.exists(self.wrkdir):
            os.mkdir(self.wrkdir)
        LOG.debug("Created %s", self.wrkdir)
        # copy files
        paths = [os.path.join(self.BASEPATH,"conf","Doxyfile")]
        paths.extend(map(lambda p: os.path.join(self.TESTSPATH,p), self.FILES))
        for path in paths:
            fromFilepath = os.path.join(self.TESTSPATH, path)
            toFilepath = os.path.join(self.wrkdir, os.path.basename(path))
            LOG.debug("Copying %s to %s", fromFilepath, toFilepath)
            shutil.copyfile(fromFilepath, toFilepath)

    def tearDown(self):
        if not config.get('save', False):
            LOG.debug("Removing '%s'", self.wrkdir)
            shutil.rmtree(self.wrkdir)
        else:
            LOG.info("Directory '%s' not removed", self.wrkdir)

    def runTest(self):
        # change directory
        origdir = os.getcwd()
        LOG.debug("Changing directory to %s", self.wrkdir)
        os.chdir(self.wrkdir)
        try:
            try:
                LOG.debug("Running doxygen")
                # setup output streams
                if config.get('fg', False):
                    stdout=None
                    stderr=None
                else:
                    stdout=subprocess.PIPE
                    stderr=subprocess.PIPE
                # run
                s = subprocess.Popen(["doxygen"], 
                                     stdout=stdout,
                                     stderr=stderr)
                stdout, stderr = s.communicate()
                if LOG.isEnabledFor(logging.DEBUG):
                    LOG.debug("Output files in ./xml are %s", os.listdir('xml'))
                # check doxygen error
                if stderr is not None:
                    errlines = stderr.split("\n")
                    errlines = filter(lambda l: l.find("Error in file")>=0, errlines)
                    if len(errlines)>0:
                        self.fail("; ".join(errlines))
                # check that everything is translated
                self.checkXML()
            except TestException, e:
                LOG.debug("Error %s", e)
                raise
                #self.fail(e)
            except Exception, e:
                LOG.debug("Error %s", e)
                raise

        finally:
            os.chdir(origdir)

    def getDoc(self, filename):
        "Get XML document for the file."
        if self.docs.has_key(filename):
            return self.docs[filename]
        filepath = os.path.join(self.path, filename)
        # check that the file exists
        if not os.path.exists(filepath):
            raise TestException("File %s does not exist" % (filepath))
        try:
            LOG.debug("Reading file %s" % filepath)
            doc = libxml2.parseFile(filepath)
        except Exception, e:
            raise TestException("XML parse of file '%s' failed: %s" %(filename, str(e)))
        self.docs[filename] = doc
        return doc

    def getFileDoc(self, name):
        "Get XML document for Fortran file."

        name = name.replace("_", "__") # doxygen doubles underscores (?)
        parts = name.split(".")
        basename = ".".join(parts[:-1])
        ext = parts[-1]
        filename = "%s_8%s.xml" % (basename, ext)
        return self.getDoc(filename)

    def getModuleDoc(self, name):
        "Get XML document for Fortran module."

        name = name.replace("_", "__") # doxygen doubles underscores (?)
        filename = "class%s.xml" % name
        return self.getDoc(filename)
    
    def getModule(self, name):
        "Get Fortran module XML element from its document."
        doc = self.getModuleDoc(name)
        modules = doc.xpathEval("doxygen/compounddef[@kind='module'][compoundname='%s']"%name)
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

        subprograms = compound.xpathEval("sectiondef[@kind='func']/memberdef[@kind='function'][name='%s']"%subprogramName.lower())
        self.assertEqual(len(subprograms),1, "%s not found" % subprogramName.lower())
        return subprograms[0]

    def getSubprogramPublic(self, compound, subprogramName):
        "Find subprogram XML element in public-func section of the interface."

        subprograms = compound.xpathEval("sectiondef[@kind='public-func']/memberdef[@kind='function'][name='%s']"%subprogramName.lower())
        self.assertEqual(len(subprograms),1)
        return subprograms[0]

    def getParamDescription(self, subprogram, paramName):
        "Get parameter description element in subprogram element."

        desc = subprogram.xpathEval("param[defname='%s']/briefdescription"%paramName)
        if len(desc)==0:
            # try detailed description
            param = subprogram.xpathEval("detaileddescription/para/parameterlist/parameteritem[parameternamelist/parametername='%s']" % paramName)
            if len(param) > 0:
                desc = param[0].xpathEval("parameterdescription")

        return desc[0]

    def getModuleVariable(self, module, varName):
        "Get variable entity."
        var = module.xpathEval("sectiondef[@kind='public-attrib']/memberdef[@kind='variable'][name='%s']"%varName.lower())
        self.assertEqual(len(var),1, "Module variable '%s' not found" % (varName))
        return var[0]

    def getBriefDescription(self, element):
        "Get brief description."
        return element.xpathEval("briefdescription")[0]

    def getInbodyDescription(self, element):
        "Get inbody description."
        return element.xpathEval("inbodydescription")[0]

    def getVarDescription(self, module, varName):
        "Get variable description entity in module."
        var = self.getModuleVariable(module, varName)
        desc = var.xpathEval("briefdescription")
        self.assertEqual(len(desc),1)
        return desc[0]

    def getInnerInterface(self,  module, intfName):
        "Get Fortran interface."

        moduleName = module.xpathEval("compoundname")[0].getContent()
        intfNameFull = "%s::%s" % (moduleName.lower(),intfName.lower())
        try:
            intfRef = module.xpathEval("*[self::innerclass='%s']" % 
                                       intfNameFull)[0]
        except IndexError, e:
            raise TestException("Interface '%s' not found in module '%s'" %
                                (intfNameFull,moduleName))
        refid = intfRef.prop('refid')
        intfDoc = self.getDoc("%s.xml" % refid)
        intf = intfDoc.xpathEval("doxygen/compounddef[@id='%s'][compoundname='%s']" % 
                                 (refid,intfNameFull))
        return intf[0]

import fortran
