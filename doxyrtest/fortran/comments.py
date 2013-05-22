import doxyrtest as rtest

class backward_f90(rtest.FortranTestCase):
    FILES = ["comments/backward.f90"]

    def runTest(self):
        file = self.getFile("backward.f90")
        sub = self.getSubprogram(file, "f")
        desc = self.getParamDescription(sub,"x")
        self.assertEqual(desc.getContent().strip(), "unused variable")

class outofplace_f90(rtest.FortranTestCase):
    "Test out-of-place documentation. See bug 522489."
    FILES = ["comments/outofplace.f90"]

    def test_nokeyword(self):
        "Just function name is specified."
        file = self.getFile("outofplace.f90")
        # no keyword specified
        sub = self.getSubprogram(file, "f")
        desc = self.getBriefDescription(sub)
        self.assertEqual(desc.getContent().strip(), "no keyword function")

    def test_funckeyword(self):
        "Function keyword is specified before the function name."
        file = self.getFile("outofplace.f90")
        # function keyword specified
        sub = self.getSubprogram(file, "f_proto")
        desc = self.getBriefDescription(sub)
        self.assertEqual(desc.getContent().strip(), "my function")
        pdesc = self.getParamDescription(sub,"a")
        self.assertEqual(pdesc.getContent().strip(), "1st parameter")
        pdesc = self.getParamDescription(sub,"b")
        self.assertEqual(pdesc.getContent().strip(), "2nd parameter")

    def test_modsubroutine(self):
        "Module scope :: specified before subroutine name without the keyword."
        mod = self.getModule("outofplace_m")
        sub = self.getSubprogramPublic(mod, "s")
        desc = self.getBriefDescription(sub)
        self.assertEqual(desc.getContent().strip(), "module subroutine")

    def test_modvar(self):
        "Module variable"
        mod = self.getModule("outofplace_m")
        var = self.getModuleVariable(mod, "v")
        desc = self.getBriefDescription(var)
        self.assertEqual(desc.getContent().strip(), "module variable")

class inbody_f90(rtest.FortranTestCase):
    "In-body comments."
    FILES = ["comments/inbody.f90"]

    def runTest(self):
        file = self.getFile("inbody.f90")
        sub = self.getSubprogram(file, "inbody_test")
        desc = self.getInbodyDescription(sub)
        self.assertEqual(desc.getContent().strip(),
            "inside the do loop !! short inside loop"
            "at the call foo")
