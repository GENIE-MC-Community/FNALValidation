#!/bin/bash

while getopts b:d:p:t: OPT
do
  case ${OPT} in
    b) # last genie build
      build=$OPTARG
      ;;
    d) # destination folder for the output
      dir=$OPTARG
      ;;
    p) # incoming particle PDG
      particle=$OPTARG
      ;;
    t) # target PDG
      target=$OPTARG
      ;;
  esac
done

source /grid/fermiapp/genie/scripts/setupGENIE.sh $build

mkdir -p jobOutput/splines

$GENIE/bin/gmkspl -p $particle -t $target -o 'jobOutput/splines/particle_'$particle'_target_'$target'_'$build'.xml' --event-generator-list CCQE

source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh
setup ifdhc

ifdh cp -r jobOutput $dir

