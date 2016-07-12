#!/bin/bash

export GENIE=/cvmfs/fermilab.opensciencegrid.org/genie/jenkinsTest/R-2_9_0
export XSECSPLINEDIR=/cvmfs/fermilab.opensciencegrid.org/genie/jenkinsTest/data

export GUPSBASE=/cvmfs/fermilab.opensciencegrid.org/

source $GUPSBASE/products/genie/externals/setup

setup root v5_34_25a -q debug:e7:nu
setup lhapdf v5_9_1b -q debug:e7
setup log4cpp v1_1_1b -q debug:e7

export LD_LIBRARY_PATH=$GENIE/lib:$LD_LIBRARY_PATH

mkdir out

$GENIE/bin/gevgen_hadron -p 211 -t 1000060120 -k 0.15 -n 10 -m hN2014 -o out/gntp_test

source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh
setup ifdhc

echo $1

ifdh cp -r out $1

