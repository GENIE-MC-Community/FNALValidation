#!/bin/bash

group='genie'        # as which group the job should be submitted (genie or fermilab)
script='runGENIE.sh' # path to the script to submit 
options=''           # possible args for script

usage ()
{
  echo
  echo './submitGENIE.sh [options]'
  echo
  echo '-g group_name [fermilab (default), genie]'
  echo '-s path_to_script'
  echo '-o script_args'
  echo '-x where_to_run [offsite, onsite (leave empty to use both resources]'
  echo
  exit 1
}

while getopts g:s:o:x:h OPT
do
  case ${OPT} in
    g) # genie or fermilab
      group=$OPTARG
      ;;
    s) # script to submit
      script=$OPTARG
      ;;
    o) # optional args for script
      options=$OPTARG
      ;;
    x) # resource (offsite, onsite)
      grid=$OPTARG
      ;;
    h)
      usage
      ;;
    *)
      usage
  esac
done

# set up destination folder based on group

if [ "$group" == 'fermilab' ]
then
  out='/pnfs/fermilab/volatile/genie/'
elif [ "$group" == 'genie' ]
then
  out='/pnfs/genie/scratch/users/geniepro/'
else
  echo  
  echo "ERROR: wrong group"
  echo
  exit 2 
fi

# set up offsite / onsite resources based on grid flag

if [ "$grid" == 'offiste' ]
then
  resource='OFFSITE'
elif [ "$grid" == 'onsite' ]
then
  resource='DEDICATED,OPPORTUNISTIC'
else
  resource='OFFSITE,DEDICATED,OPPORTUNISTIC' 
fi

# set up jobsub
source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh
setup jobsub_client

jobsub_submit -G $group -M --OS=SL6 --resource-provides=usage_model=$resource file://$script -b $LAST_GENIE_BUILD -d $out $options
