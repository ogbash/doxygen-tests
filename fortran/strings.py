import base

class qsigns(base.FortranTestCase):
    """Question sign inside string.
    """

    FILES = ["strings/qsigns.f90"]

    def checkXML(self):
        print "RUNNING"
        file = self.getFile("qsigns.f90")

        sub = self.getSubprogram(file, "tst")
        self.assertTrue(sub is not None)
