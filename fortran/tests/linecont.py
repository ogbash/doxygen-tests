
import base

class parcomment_f90(base.FortranTestCase):
    "Line continuations within subroutine parameters."

    def checkXML(self):
        self.module = self.getModule("parcomment")
        self.check_testme1()
        self.check_testme2()

    def check_testme1(self):
        # testme1
        testme1 = self.getSubprogram(self.module,"testme1")
        argstring = testme1.xpathEval("argsstring")[0]
        self.assertEqual(argstring.getContent(), "(a, b, c, d)")

        # testme1 parameters
        for varName in ["a", "b", "c", "d"]:
            paramdesc = self.getParamDescription(testme1, varName)
            self.assertEqual(paramdesc.getContent().strip(),"variable %s"%varName)
    def check_testme2(self):
        # testme2
        testme2 = self.getSubprogram(self.module,"testme2")
        argstring = testme2.xpathEval("argsstring")[0]
        self.assertEqual(argstring.getContent(), "(a, b, c, as, bs, d)")

        # testme2 parameters
        for varName in ["a", "b", "c", "as", "bs", "d"]:
            paramdesc = self.getParamDescription(testme2, varName)
            self.assertEqual(paramdesc.getContent().strip(),"variable %s"%varName)

class varcomment_f90(base.FortranTestCase):
    "Line continuations within module variables."

    def checkXML(self):
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


class parcomment_f(base.FortranTestCase):
    "Line continuations within subroutine parameters (fixed form)."

    def checkXML(self):
        file = self.getFile("parcomment.f")
        example = self.getSubprogram(file, "example")

        desc = self.getParamDescription(example, "val")
        self.assertEqual(desc.getContent().strip(), "[in] scalar double input")

        desc = self.getParamDescription(example, "mat")
        self.assertEqual(desc.getContent().strip(), "[in,out] matrix double argument")

        desc = self.getParamDescription(example, "ierr")
        self.assertEqual(desc.getContent().strip(), "[out] error code")

