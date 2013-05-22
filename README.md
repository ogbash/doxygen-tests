This is an attempt to create regression tests for Doxygen, primarly for Fortran parser.
Under development..., the rules and the layout may change.

It requires Python 2.5 and python-libxml2.

RUNNING TESTS
=============
In the root directory to run all Fortran tests or specific test:

    ./test.py fortran
    ./test.py fortran.blocks.interface_op_f90

This runs the tests and cleans all input and output files. If you want to preserve and inspect the output files use -d <outdir> command line argument to supress temporary directory:

    ./test.py -d out --fg fortran.comments.outofplace_f90

This directory is not cleaned (deleted) every time test is executed, so there may be false positives. You should clean it yourself when it is necessary.

The --fg also redirects Doxygen output to standard output. 

EFFECTS
-------
Without -d option the script creates separate temporary directory for every test *class*. Fortran file(s) and Doxyfile are copied to the directory. Doxygen is run in the directory and XML output is written to 'xml' subdirectory. Finally, corresponding Python test is executed. The temporary directory is deleted at the end.


WRITING TESTS
=============
Place new Fortran file into one of the tests/fortran/ directories: syntax/, blocks/, linecont/, or other. Create or update the corresponding Python file in the `doxyrtest/fortran/` directory:
 1. create test class that extends doxyrtest.FortranTestCase
 2. specify input `FILES = ["subdir/program.f90"]` in the class
 3. define runTest(self) method or several test_*(self) methods
    * use `self.getModule(name)` to fetch libxml2 XML element instance for module
      * if there was an error during doxygen execution it is thrown
      * there is a set of predefined methods in FortranTestCase
    * use `elem.xpathEval("...")` to fetch other elements
    * use `self.assertTrue()`, `self.assertEqual()`, ... to verify fetched values

XPath standard:
http://www.w3.org/TR/xpath/
Check "2.5 Abbreviated Syntax" before writing your tests.
