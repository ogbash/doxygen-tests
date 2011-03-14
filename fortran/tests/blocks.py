
import base

class interface_spec_f90(base.FortranTestCase):
    """See bug 637610.

    Specific interfaces are listed in an INTERFACE block without a (generic)
    name after INTERFACE; multiple interfaces may be listed in one INTERFACE 
    block.
    """

    def runTest(self):
        interface_spec = self.getModule("interface_spec")

        for name in ["g", "f"]:
            gIntf = self.getInnerInterface(interface_spec, name)

            # only one subprogram in the interface
            subs = gIntf.xpathEval("sectiondef/memberdef")
            self.assertEqual(len(subs),1)

            # its name is _name_
            gSub = self.getSubprogramPublic(gIntf, name)
        

class interface_gen_f90(base.FortranTestCase):
    """See bug 637610.

    Generic INTERFACEs have a generic name, all INTERFACEs should be listed
    under this name in documentation.
    """

    def runTest(self):
        interface_spec = self.getModule("interface_gen")
        
        gIntf = self.getInnerInterface(interface_spec, "f")
        # 2 subprograms in the interface
        subs = gIntf.xpathEval("sectiondef/memberdef")
        self.assertEqual(len(subs),2)

        for name in ["f4", "f8"]:
            # subprogram with name is present
            gSub = self.getSubprogramPublic(gIntf, name)
        
class interface_abst_f90(base.FortranTestCase):
    """See bug 637610.

    Like specific interfaces, ABSTRACT interfaces do not have a generic name
    and multiple interfaces may be listed in one interface block.
    """

    def runTest(self):
        interface_spec = self.getModule("interface_abst")

        for name in ["s", "f"]:
            gIntf = self.getInnerInterface(interface_spec, name)

            # only one subprogram in the interface
            subs = gIntf.xpathEval("sectiondef/memberdef")
            self.assertEqual(len(subs),1)

            # its name is _name_
            gSub = self.getSubprogramPublic(gIntf, name)
        
