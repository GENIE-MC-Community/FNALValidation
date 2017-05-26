#!/bin/bash
# generate a list of job ids based on user name, looking for the "runGENIE" script name and turn them into a long csv string.
# then go remove all the jobs with those ids...
jobsub_rm -G genie --role=Analysis  --jobid="`jobsub_q --user $USER -G genie | grep "runGENIE" | grep "H" | cut -d ' ' -f 1 | tr '\n' ','`"
