#!/usr/bin/env python
"""
Retrieve build from Jenkins.

    python getJenkinsBuildToDisk.py --genie_tag <tag> --builds <path>

e.g.:
    export BUILDD=/grid/fermiapp/genie/builds
    python getJenkinsBuildToDisk.py --genie_tag trunk --builds $BUILDD

Or:
    export BUILDD=/grid/fermiapp/genie/builds
    python getJenkinsBuildToDisk.py --genie_tag R-2_10_8 --builds $BUILDD
"""

from jobsub import Jobsub
import parser, jenkins, msg, nun, nua, standard, reptest, xsecval, hadronization
import os, datetime

def initMessage (args):
    print msg.BLUE
    print '*' * 29
    print '*', ' ' * 25, '*'
    print "*\tGENIE Validation", ' ' * 2, '*'
    print '*', ' ' * 25, '*'
    print '*' * 29
    print msg.GREEN
    print "Configuration:\n"
    print "\tGENIE version:\t", args.tag
    print "\tBuild on:\t", args.build_date
    print "\tLocated at:\t", args.builds
    print msg.END
    
if __name__ == "__main__":
    # parse command line arguments
    args = parser.getArgs(require_output_path=False, require_run_path=False,
                          usage=__doc__)
    # find most recent build if date was not defined
    if args.build_date is None: 
        args.build_date = jenkins.findLast(args.tag)
    # print configuration summary
    initMessage(args)
    # get build
    msg.info ("Getting GENIE from jenkins...\n")
    args.buildName = jenkins.getBuild(args.tag, args.build_date, args.builds)
