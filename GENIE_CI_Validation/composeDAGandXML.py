#!/usr/bin/env python

from jobsub import Jobsub
# services
import parser, msg
import outputPaths
# xsec splines
import nun, nua
# "sanity check" (events scan)
import standard
# old-style validation
import hadronization
# new-style validation (minerva, etc.)
import xsecval, minerva
# general
import os, datetime

# example format:
# ./runLegacyValidation.py --genie_tag trunk  \ 
#                          --build_date YYYY-MM-DD  \
#                          --run_path /path/to/runGENIE.sh \ # e.g. /grid/fermiapp/genie/legacyValidation_update_1/runGENIE.sh
#                          --builds DUMMY \ 
#                          --output OUTPUT \ # e.g. /pnfs/genie/scratch/users/yarba_j/GENIE_LegacyValidation 
#  optional:               [ --regre 'R-2_12_6/2017-09-11 [reg2, reg3,...]' --regre_dir /pnfs/genie/persistent/users/yarba_j/GENIE_LegacyValidation ]

def initMessage (args):
  print msg.BLUE
  print '*' * 80
  print '*', ' ' * 76, '*'
  print "*\tGENIE Legacy Validation based on src/scripts/production/batch", ' ' * 8, '*'
  print '*', ' ' * 76, '*'
  print '*' * 80
  print msg.GREEN
  print "Configuration:\n"
  print "\tGENIE version:\t", args.tag
  print "\tBuild on:\t", args.build_date
  print "\tLocated at:\t", args.builds
  print "\n\tResults folder:", args.output
  print msg.END

if __name__ == "__main__":
  
  
  # parse command line arguments
  args = parser.getArgs()
  print "CHECK DATE: ", args.build_date
  # if build date is not defined/specified, use today's date as default
  if args.build_date is None:
     print "DATE is None, reseting it to DEFAULT(today)"
     #
     # NOTE-1: os.system('date +%Y-%m-%d') will return an integer status !!!
     # NOTE-2: os.popen('date +%Y-%m-%d').read() will results in the "?" question mark at the end of the string
     # NOTE-3: the "%y-%m-%d" will result in the YY-MM-DD format
     #
     args.build_date = datetime.date.today().strftime("%Y-%m-%d") 
  
  # print configuration summary
  initMessage (args)

  # preapre folder(s) structure for output
  args.paths = outputPaths.prepare (args.output + "/" + args.tag + "/" + args.build_date)

  # initialize jobsub 
  #
  # NOTE: at this point, we are using it only to fill up DAGs;
  #       we are not submitting anything...
  #       ...maybe the DGA-filling part needs to make into a separate module ?
  #
  args.buildNameGE = "generator_" + args.tag + "_" + args.build_date
  args.buildNameCmp = "comparisons_" + args.cmptag + "_" + args.build_date

  # regresion tests (optional)
  if not (args.regretags is None):
     args.regretags = args.regretags.split()
     # also need to check/assert that args.regredir is not None !!! otherwise throw !!!
     # assert ( not (args.regredir is None) ), "Path to regression dir is required for regression tests"
     if args.regredir is None: raise AssertionError

  jobsub = Jobsub (args)

  # fill dag files with jobs
  msg.info ("Adding jobs to dag file: " + jobsub.dagFile + "\n")
  # nucleon cross sections
  nun.fillDAG ( jobsub, args.tag, args.paths )
  # nucleus cross sections
  nua.fillDAG ( jobsub, args.tag, args.paths )
  # standard mc sanity check (events scan)
  standard.fillDAG( jobsub, args.tag, args.paths )
  # xsec validation
  xsecval.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.regretags, args.regredir )
  # hadronization test
  hadronization.fillDAG (jobsub, args.tag, args.build_date, args.paths )
  # MINERvA test
  minerva.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.regretags, args.regredir )
