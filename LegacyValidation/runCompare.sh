#!/bin/bash

while getopts p:v:f:o:c: OPT
do
  case ${OPT} in
    p) # path to genie top dir
      export GENIE=$OPTARG
      ;;
    v) # path to comparisons top dir
      export GENIE_COMPARISONS=$OPTARG
      ;;
    f) # xml filelist
      xml=$OPTARG
      ;;
    o) # output
      out=$OPTARG
      ;;
    c) # command to run
      com=$OPTARG
      ;;
  esac
done

### setup externals and paths ###

## out of date...
# export GUPSBASE=/cvmfs/fermilab.opensciencegrid.org/
# source $GUPSBASE/products/genie/externals/setup
# setup root v5_34_25a -q debug:e7:nu
# setup lhapdf v5_9_1b -q debug:e7
# setup log4cpp v1_1_1b -q debug:e7

## use larsoft...
source /grid/fermiapp/products/genie/bootstrap_genie_ups.sh
# These don't need to be debug 
#
#setup root v5_34_25a -q debug:e7:nu
#setup lhapdf v5_9_1b -q debug:e7
#setup log4cpp v1_1_1b -q debug:e7
#
# switch to the optimized ones
#
setup root v5_34_25a -q e7:nu:prof
setup lhapdf v5_9_1b -q e7:prof
setup log4cpp v1_1_1b -q e7:prof

echo " GENIE = $GENIE "
echo " GENIE_COMPARISONS = $GENIE_COMPARISONS "

ls -alF $GENIE_COMPARISONS/bin

export LD_LIBRARY_PATH=$GENIE/lib:$GENIE_COMPARISONS/lib:$LD_LIBRARY_PATH
export PATH=$GENIE/bin:$GENIE_COMPARISONS/bin:$PATH

echo " command = $com "

$com -g $xml -o $out
