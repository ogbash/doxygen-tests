import doxyrtest as rtest

class qsigns(rtest.FortranTestCase):
    """Question sign inside string.
    """

    FILES = ["strings/qsigns.f90"]

    def runTest(self):
        file = self.getFile("qsigns.f90")

class nobackslash(rtest.FortranTestCase):
    "Backslashes inside a string."
    FILES = ["strings/nobackslash.f90"]

    def runTest(self):
        file = self.getFile("nobackslash.f90")

