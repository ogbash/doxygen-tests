
import base

class backward_f90(base.FortranTestCase):

    def checkXML(self):
        file = self.getFile("backward.f90")
        sub = self.getSubprogram(file, "f")
        desc = self.getParamDescription(sub,"x")
        self.assertEqual(desc.getContent().strip(), "unused variable")


