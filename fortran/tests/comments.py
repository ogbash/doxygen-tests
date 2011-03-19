
import base

class backward_f90(base.FortranTestCase):

    def checkXML(self):
        file = self.getFile("backward.f90")
        sub = self.getSubprogram(file, "f")
        desc = self.getParamDescription(sub,"x")
        self.assertEqual(desc.getContent().strip(), "unused variable")

class outofplace_f90(base.FortranTestCase):

    def checkXML(self):
        file = self.getFile("outofplace.f90")
        sub = self.getSubprogram(file, "f_proto")
        desc = self.getBriefDescription(sub)
        self.assertEqual(desc.getContent().strip(), "my function")
        pdesc = self.getParamDescription(sub,"a")
        self.assertEqual(pdesc.getContent().strip(), "1st parameter")
        pdesc = self.getParamDescription(sub,"b")
        self.assertEqual(pdesc.getContent().strip(), "2nd parameter")

class inbody_f90(base.FortranTestCase):
    "In-body comments."
    def checkXML(self):
        file = self.getFile("inbody.f90")
        sub = self.getSubprogram(file, "inbody_test")
        desc = self.getInbodyDescription(sub)
        self.assertEqual(desc.getContent().strip(),
            "inside the do loop !! short inside loop"
            "at the call foo")
