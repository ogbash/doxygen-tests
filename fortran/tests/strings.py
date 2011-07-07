import base

class qsign(base.FortranTestCase):
    """Question sign inside string.
    """

    def checkXML(self):
        print "RUNNING"
        file = self.getFile("qsigns.f90")

        sub = self.getSubprogram(file, "tst")
        self.assertTrue(sub is not None)
