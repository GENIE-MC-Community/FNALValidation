#!/usr/bin/env python

# GENIE Legacy Validation based on src/scripts/production/batch

# example format:
# ./runLegacyValidation.py --genie_tag R-2_12_0  \ 
#                          --run_path /grid/fermiapp/genie/legacyValidation_update_1/runGENIE.sh \
#                          --builds /grid/fermiapp/genie/builds_update \ 
#                          --output /pnfs/genie/scratch/users/yarba_j/GENIE_LegacyValidation

from jobsub import Jobsub
# various services
import parser, jenkins, msg 
# xsec splines
import nun, nua
# old-style (legacy) validation tests
import standard, reptest, xsecval, hadronization
# new-style validation (minerva, etc.)
import minerva
# general
import os, datetime

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

def preparePaths (path):
  # create a dictionary for output paths
  paths = {}
  paths['top'] = path
  # splines
  paths['xsec']   = path + "/xsec"
  paths['xsec_N'] = path + "/xsec/nuN"
  paths['xsec_A'] = path + "/xsec/nuA"
  # events
  paths['events']  = path + "/events"
  paths['mctest']  = path + "/events/mctest"
  paths['reptest'] = path + "/events/repeatability"
  paths['xsecval'] = path + "/events/xsec_validation"
  paths['hadron']  = path + "/events/hadronization"
  paths['minerva'] = path + "/events/minerva"
  # reports
  paths['reports'] = path + "/reports"
  paths['sanity']  = path + "/reports/sanity_mctest"
  paths['replog']  = path + "/reports/repeatability_test"
  paths['xseclog'] = path + "/reports/xsec_validation"
  paths['xsecsng'] = path + "/reports/xsec_validation/single_comparisons_with_errors"
  paths['hadrep']  = path + "/reports/hadronization_test"
  paths['minervarep'] = path + "/reports/minerva"
  # create all directiories
  for p in paths.values():
    if not os.path.exists (p): os.makedirs (p)
  # return paths dictionary
  return paths
    
if __name__ == "__main__":
  # parse command line arguments
  args = parser.getArgs()
  #
  # find most recent build if date was not defined 
  # NOTE: need to check if the two build dates are consistent !       
  if args.build_date is None:
     args.build_date = jenkins.findLast("generator",args.tag)
     args.build_date = jenkins.findLast("comparisons",args.cmptag)
  # print configuration summary
  initMessage (args)
  #
  # print configuration summary
  msg.info ("Getting GENIE from jenkins...\n")
  # get build
  args.buildNameGE  = jenkins.getBuild ("generator",args.tag, args.build_date, args.builds)
  args.buildNameCmp = jenkins.getBuild ("comparisons",args.cmptag, args.build_date, args.builds)
  # preapre folder structure for output
  args.paths = preparePaths (args.output + "/" + args.tag + "/" + args.build_date)
  # initialize jobsub
  jobsub = Jobsub (args)

  # fill dag files with jobs
  msg.info ("Adding jobs to dag file: " + jobsub.dagFile + "\n")
  # nucleon cross sections - always do this
  nun.fillDAG (jobsub, args.tag, args.paths)

  # set optional pieces
  do_nucleus = True
  do_mctest = True
  do_repeat = True
  do_xsec_val = True
  do_hadro = True
  do_minerva = True

  # nucleus cross sections
  if do_nucleus:
    nua.fillDAG (jobsub, args.tag, args.paths)
  # standard mctest sanity
  if do_mctest:
    standard.fillDAG (jobsub, args.tag, args.paths)
  # repeatability test
  if do_repeat:
    reptest.fillDAG (jobsub, args.tag, args.paths)
  # xsec validation
  if do_xsec_val:
    xsecval.fillDAG (jobsub, args.tag, args.build_date, args.paths)
  # hadronization test
  if do_hadro:
    hadronization.fillDAG (jobsub, args.tag, args.build_date, args.paths)
  # MINERvA test
  if do_minerva:
    minerva.fillDAG( jobsub, args.tag, args.build_date, args.paths, args.builds+"/"+args.buildNameCmp )
  # dag file done, submit jobs
  jobsub.submit()
