import doxyrtest as rtest

class parcomment_f90(rtest.FortranTestCase):
    "Line continuations within subroutine parameters."

    FILES = ["linecont/parcomment.f90"]

    def test_me1(self):
        # testme1
        self.module = self.getModule("parcomment")
        testme1 = self.getSubprogramPublic(self.module,"testme1")
        argstring = testme1.xpathEval("argsstring")[0]
        self.assertEqual(argstring.getContent(), "(a, b, c, d)")

        # testme1 parameters
        for varName in ["a", "b", "c", "d"]:
            paramdesc = self.getParamDescription(testme1, varName)
            self.assertEqual(paramdesc.getContent().strip(),"variable %s"%varName)

    def test_me2(self):
        # testme2
        self.module = self.getModule("parcomment")
        testme2 = self.getSubprogramPublic(self.module,"testme2")
        argstring = testme2.xpathEval("argsstring")[0]
        self.assertEqual(argstring.getContent(), "(a, b, c, as, bs, d)")

        # testme2 parameters
        for varName in ["a", "b", "c", "as", "bs", "d"]:
            paramdesc = self.getParamDescription(testme2, varName)
            self.assertEqual(paramdesc.getContent().strip(),"variable %s"%varName)

class varcomment_f90(rtest.FortranTestCase):
    "Line continuations within module variables."

    FILES = ["linecont/varcomment.f90"]

    def runTest(self):
        varcomment = self.getModule("varcomment")
        
        for varName in ["a", "b", "c", "as", "bs", "d"]:
            desc = self.getVarDescription(varcomment, varName)
            self.assertEqual(desc.getContent().strip(), "variable %s"%varName)

        var = self.getModuleVariable(varcomment, "as")
        self.assertEqual(var.xpathEval("type")[0].getContent().strip(),
                         "integer, dimension(:,:), pointer")

        for init in [1,2,3]:
            desc = self.getVarDescription(varcomment, "i%d"%init)
            self.assertEqual(desc.getContent().strip(), "variable with init%d"%init)


class parcomment_f(rtest.FortranTestCase):
    "Line continuations within subroutine parameters (fixed form)."

    FILES = ["linecont/parcomment.f"]

    def runTest(self):
        file = self.getFile("parcomment.f")
        example = self.getSubprogram(file, "example")

        desc = self.getParamDescription(example, "val")
        self.assertEqual(desc.getContent().strip(), "[in] scalar double input")

        desc = self.getParamDescription(example, "mat")
        self.assertEqual(desc.getContent().strip(), "[in,out] matrix double argument")

        desc = self.getParamDescription(example, "ierr")
        self.assertEqual(desc.getContent().strip(), "[out] error code")

class fixed_f(rtest.FortranTestCase):
    "Different symbols for line continuation in fixed form."

    FILES = ["linecont/fixed.f"]

    def runTest(self):
        file = self.getFile("fixed.f")
        functions = file.xpathEval("sectiondef[@kind='func']/memberdef")
        self.assertEqual(len(functions), 35)

        # every function has 2 parameters
        for n in range(0,10)+map(chr,range(ord('A'),ord('X')+1)):
            name = "foo%s"%n
            sub = self.getSubprogram(file, name)
            params = sub.xpathEval("param")
            self.assertEquals(len(params),2)
