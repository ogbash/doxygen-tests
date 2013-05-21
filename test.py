#! /usr/bin/env python

import logging
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

import sys
import getopt

def printUsage():
    sys.stderr.write("""Usage: ./test.py [-h --help] [--fg] [-d <outdir>] <testpath>, where 'path' is module, class or method path.
\t-h,--help\tthis message
\t-d <outdir>\tleave output files in the directory
\t--fg\t\trun doxygen in foreground, this should be used only for special runs,
\t\t\tbecause test results may depend on doxygen output
""")

# define options
opts,args = getopt.getopt(sys.argv[1:],
                          "-hd:",
                          ["help","fg"])
opts = dict(opts)

if opts.has_key('-h') or opts.has_key('--help'):
    printUsage()
    sys.exit(0)

if len(args)!=1:
    printUsage()
    sys.exit(1)
testname = args[0]

# extract options
import fortran.base as base
if opts.has_key('-d'):
    base.config['outdir'] = opts['-d']
    base.config['save'] = True
if opts.has_key('--fg'):
    base.config['fg'] = True

import unittest
loader = unittest.defaultTestLoader
suite = loader.loadTestsFromName(testname)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
