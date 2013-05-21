import base

class qsigns(base.FortranTestCase):
    """Question sign inside string.
    """

    FILES = ["strings/qsigns.f90"]

    def checkXML(self):
        file = self.getFile("qsigns.f90")

class nobackslash(base.FortranTestCase):
    "Backslashes inside a string."
    FILES = ["strings/nobackslash.f90"]

    def checkXML(self):
        file = self.getFile("nobackslash.f90")

