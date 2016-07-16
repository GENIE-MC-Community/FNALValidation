#!/bin/bash
export GUPSBASE=/cvmfs/fermilab.opensciencegrid.org/
source $GUPSBASE/products/genie/externals/setup
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh
setup ifdhc
setup jobsub_client
