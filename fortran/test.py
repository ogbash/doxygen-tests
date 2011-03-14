#! /usr/bin/env python
import sys
import tests

if len(sys.argv)<2:
    sys.stderr.write("Usage: %s <test name>, where the name is module, class or method path.\n" % sys.argv[0])
    sys.exit(1)
testname = sys.argv[1]

import unittest
loader = unittest.defaultTestLoader
suite = loader.loadTestsFromName(testname)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
