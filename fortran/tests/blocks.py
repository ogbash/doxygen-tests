
import base

class interface_spec_f90(base.FortranTestCase):
    """See bug 637610.

    Specific interfaces are listed in an INTERFACE block without a (generic)
    name after INTERFACE; multiple interfaces may be listed in one INTERFACE 
    block.
    """

    def runTest(self):
        module = self.getModule("interface_spec")

        for name in ["g", "f"]:
            intf = self.getInnerInterface(module, name)

            # only one subprogram in the interface
            subs = intf.xpathEval("sectiondef/memberdef")
            self.assertEqual(len(subs),1)

            # its name is _name_
            self.assertTrue(self.getSubprogramPublic(intf, name) is not None)
        

class interface_gen_f90(base.FortranTestCase):
    """See bug 637610.

    Generic INTERFACEs have a generic name, all INTERFACEs should be listed
    under this name in documentation.
    """

    def runTest(self):
        module = self.getModule("interface_gen")
        
        intf = self.getInnerInterface(module, "f")
        # 2 subprograms in the interface
        subs = intf.xpathEval("sectiondef/memberdef")
        self.assertEqual(len(subs),2)

        for name in ["f4", "f8"]:
            # subprogram with name is present
            self.assertTrue(self.getSubprogramPublic(intf, name) is not None)
        
class interface_abst_f90(base.FortranTestCase):
    """See bug 637610.

    Like specific interfaces, ABSTRACT interfaces do not have a generic name
    and multiple interfaces may be listed in one interface block.
    """

    def runTest(self):
        module = self.getModule("interface_abst")

        for name in ["s", "f"]:
            intf = self.getInnerInterface(module, name)

            # only one subprogram in the interface
            subs = intf.xpathEval("sectiondef/memberdef")
            self.assertEqual(len(subs),1)

            # its name is _name_
            self.assertTrue(self.getSubprogramPublic(intf, name) is not None)
        
class interface_op_f90(base.FortranTestCase):
    """See bug 630582.

    END INTERFACE OPERATOR in fortran 90 crashes Doxygen
    """

    def runTest(self):
        module = self.getModule("interface_op")

        intf = self.getInnerInterface(module, "OPERATOR(*)")

        # only one subprogram in the interface
        subs = intf.xpathEval("sectiondef/memberdef")
        self.assertEqual(len(subs),1)

        # vect_prod is present
        self.assertTrue(self.getSubprogramPublic(intf, "vect_prod") is not None)
