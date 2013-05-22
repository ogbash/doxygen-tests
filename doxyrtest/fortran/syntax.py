
import doxyrtest as rtest

# general syntax

class label_endsub(rtest.FortranTestCase):
    """Allow label before end statement, see bug 626476.
    """

    FILES = ["syntax/label_endsub.f90"]

    def runTest(self):
        file = self.getFile("label_endsub.f90")

        sub = self.getSubprogram(file, "tst")
        self.assertTrue(sub is not None)
