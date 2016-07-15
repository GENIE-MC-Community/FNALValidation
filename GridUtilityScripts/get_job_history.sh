#!/bin/bash
#
# expect output like:
# ------------------
# JOBSUBJOBID                             OWNER                SUBMITTED           FINISHED            ST       CMD
# 12160094.0@fifebatc2.fnal.gov          perdue               2016-07-14 14:52:49 2016-07-14 14:54:18 C        runGENIE.s
# ...
# 28 jobs; 15 completed, 13 removed, 0 idle, 0 running, 0 eld, 0 suspended
# ------------------
# So, filter output into a whitespace split and match lines with <#####>.0 in them.
jobsub_history -G genie --user $USER | perl -ne '@l=split("\h",$_); if (/(\d+).0/) { print @l[0]."\n"; }'
