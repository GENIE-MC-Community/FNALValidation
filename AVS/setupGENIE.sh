#!/bin/bash

#GENIEBASE=/cvmfs/fermilab.opensciencegrid.org/genie/

GENIEBASE=/grid/fermiapp/genie/

ls $GENIEBASE

export GENIE=$GENIEBASE/builds/$1/

export GUPSBASE=/cvmfs/fermilab.opensciencegrid.org/

source $GUPSBASE/products/genie/externals/setup

setup root v5_34_25a -q debug:e7:nu
setup lhapdf v5_9_1b -q debug:e7
setup log4cpp v1_1_1b -q debug:e7

export LD_LIBRARY_PATH=$GENIE/lib:$LD_LIBRARY_PATH
