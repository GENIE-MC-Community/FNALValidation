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
# new-style validation (sec, minerva, t2k, etc.)
import xsecval, minerva, t2k
# general
import os, datetime

# example format:
# ./composeDAGandXML.py --genie_tag trunk  \ 
#                          --build_date YYYY-MM-DD  \
#                          --run_path /path/to/runGENIE.sh \ # e.g. /grid/fermiapp/genie/legacyValidation_update_1/runGENIE.sh
#                          --builds DUMMY \ 
#                          --output OUTPUT \ # e.g. /pnfs/genie/scratch/users/yarba_j/GENIE_LegacyValidation 
#  optional:               [ --tunes tune1,tune2,...]  # comma-separated !!!
#  optional:               [ --regre R-2_12_6/2017-09-11,RegTag2,RegTag3,... --regre_dir /pnfs/genie/persistent/users/yarba_j/GENIE_LegacyValidation ]
#
# OLD FORMAT !!! 
#  optional:               [ --tunes 'tune1 tune2 ...' ]
#  optional:               [ --regre 'R-2_12_6/2017-09-11 [reg2 reg3...]' --regre_dir /pnfs/genie/persistent/users/yarba_j/GENIE_LegacyValidation ]

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
  args.paths = outputPaths.prepare ( args.output + "/" + args.tag + "/" + args.build_date )

  # initialize jobsub 
  #
  # NOTE: at this point, we are using it only to fill up DAGs;
  #       we are not submitting anything...
  #       ...maybe the DGA-filling part needs to make into a separate module ?
  #
  args.buildNameGE = "generator_" + args.tag + "_" + args.build_date
  args.buildNameCmp = "comparisons_" + args.cmptag + "_" + args.build_date

  # tune(s) (optional)
  if not (args.tunes is None):
     args.tunes = args.tunes.split(",")
  
  # regresion tests (optional)
  if not (args.regretags is None):
     args.regretags = args.regretags.split(",")
     # also need to check/assert that args.regredir is not None !!! otherwise throw !!!
     # assert ( not (args.regredir is None) ), "Path to regression dir is required for regression tests"
     if args.regredir is None: raise AssertionError

  jobsub = Jobsub (args)

  # fill dag files with jobs
  msg.info ("Adding jobs to dag file: " + jobsub.dagFile + "\n")
  # nucleon cross sections
  nun.fillDAG ( jobsub, args.tag, args.paths, args.tunes )
  # nucleus cross sections
  nua.fillDAG ( jobsub, args.tag, args.paths, args.tunes )
  # standard mc sanity check (events scan)
  # ---> standard.fillDAG( jobsub, args.tag, args.paths ) # NO TUNES assumed so far !!!
  # xsec validation
  # ---> xsecval.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.regretags, args.regredir ) # NO TUNES assumed so far
  # hadronization test
  # ---> hadronization.fillDAG ( jobsub, args.tag, args.build_date, args.paths, args.tunes, args.regretags, args.regredir )
  # MINERvA test
  # ---> minerva.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.tunes, args.regretags, args.regredir )
  # T2K
  # t2k.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.tunes, args.regretags, args.regredir )
