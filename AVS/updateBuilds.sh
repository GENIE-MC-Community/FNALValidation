#!/bin/bash

export PATH=$PATH:/usr/krb5/bin/

export GENIE_SCRIPTS=/grid/fermiapp/genie/scripts

source $GENIE_SCRIPTS/getGenieFromJenkins.sh

cd $GENIE_BUILDS; mkdir -p $LAST_GENIE_BUILD

tar -zxf ''$LAST_GENIE_BUILD'.tgz' --directory $LAST_GENIE_BUILD

rm ''$LAST_GENIE_BUILD'.tgz'

cd $GENIE_SCRIPTS

sleep 12h

./submitGENIE.sh -s 'generateSplines.sh' -o '-p 14 -t 1000060120' -x onsite
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p 14 -t 1000060120'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p 14 -t 1000260560'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p -14 -t 1000060120'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p -14 -t 1000260560'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p 12 -t 1000060120'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p 12 -t 1000260560'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p -12 -t 1000060120'
#./submitGENIE.sh -s 'generateSplines.sh' -o '-p -12 -t 1000260560'
