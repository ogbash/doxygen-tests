
import base

# general syntax

class label_endsub(base.FortranTestCase):
    """Allow label before end statement, see bug 626476.
    """

    def runTest(self):
        file = self.getFile("label_endsub.f90")

        sub = self.getSubprogram(file, "tst")
        self.assertTrue(sub is not None)
