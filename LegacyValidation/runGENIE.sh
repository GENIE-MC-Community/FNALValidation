#!/bin/bash

while getopts p:o:i:l:c:d: OPT
do
    case ${OPT} in
        p) # path to genie top dir
            export GENIE=$OPTARG
            ;;
        o) # output directory
            out=$OPTARG
            ;;
        i) # input files (fileA fileB fileC...)
            if [ "$OPTARG" == "none" ]; then
                input=$OPTARG
            else
                input=(`echo $OPTARG | sed 's/SPACE/ /g'`)
            fi
            ;;
        l) # logfile name
            log=$OPTARG
            ;;
        d) # print out to logfile
            debug=$OPTARG
            ;;
        c) # command to run
            cmd=`echo $OPTARG | sed 's/SPACE/ /g' | sed "s/SQUOTE/'/g"` 
            ;;
    esac
done

### setup externals and paths ###

# export GUPSBASE=/cvmfs/fermilab.opensciencegrid.org/
# source $GUPSBASE/products/genie/externals/setup

# bootstrap setup off larsoft repo...
source /grid/fermiapp/products/genie/bootstrap_genie_ups.sh

setup root v5_34_25a -q debug:e7:nu
setup lhapdf v5_9_1b -q debug:e7
setup log4cpp v1_1_1b -q debug:e7

export LD_LIBRARY_PATH=$GENIE/lib:$LD_LIBRARY_PATH
export PATH=$GENIE/bin:$PATH

echo "Command: "$cmd > $log
echo "LD_LIBRARY_PATH = $LD_LIBRARY_PATH" >> $log
echo "PATH = $PATH" >> $log
echo "GENIE = $GENIE" >> $log
echo "Contents of GENIE/bin: " >> $log
echo `ls $GENIE/bin` >> $log
echo "Running command" >> $log

source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh
setup ifdhc

### load input (if defined) ###

if [ "$input" != "none" ]; then

    echo "input is not none..."
    echo "input is not none..." >> $log
    idir=`dirname "$input"` 
    ipat=`basename "$input"`
    echo "idir = $idir"
    echo "idir = $idir" >> $log
    echo "ipat = $ipat"
    echo "ipat = $ipat" >> $log
    # recall that `findMatchingFiles` recursively scans subdirs
    ifdh findMatchingFiles "$idir" "$ipat"
    ifdh findMatchingFiles "$idir" "$ipat" >> $log
    inputlist=`ifdh findMatchingFiles "$idir" "$ipat"`

    echo "making local input storage folder.."
    echo "making local input storage folder.." >> $log
    mkdir input
    echo "running ifdh fetch"
    echo "running ifdh fetch" >> $log
    IFDH_DATA_DIR=./input ifdh fetchSharedFiles $inputlist

    if [ "$debug" == "true" ]
    then
        echo "Checking contents of local input folder: "
        ls -lh input
    fi
    echo "Checking contents of local input folder: " >> $log
    ls -lh input >> $log

fi  # check `input == none`

### run the command ###

if [ "$debug" == "true" ]
then
    echo "DEBUG MODE ON. ALL OUTPUT WILL BE COPIED TO LOG FILE"
    # $cmd >> $log
    # "grid debug" -> put output into grid log file?
    $cmd
else
    $cmd 1>/dev/null 2>$log
fi

### copy results to scratch

# first, remove size zero log files
logs=`ls *.log`
for logfile in $logs
do
    echo $logfile
    if [[ ! -s $logfile ]]; then
        echo "... is a zero size file, removing!"
        rm $logfile
    fi
done

mkdir scratch
mv *.root scratch
mv *.xml scratch
mv *.log scratch
mv *.eps scratch
mv *.ps scratch
mv *.pdf scratch

if [ "$debug" == "true" ]
then
    echo "Checking output files..."
    ls scratch
fi

### copy everything from scratch to output 
# r. hatcher is dubious of `cp -r` in ifdhcp
# ifdh cp -r scratch $out

# copy files one-by-one after making any necessary subdirectories
# use -x to enable echoing commands (+x to turn it back off)
cd scratch
# make a script to be sourced ...
rm -f copy_file.sh
touch copy_files.sh
# make any subdirectories (remove leading ./)
find . -type d -exec echo ifdh mkdir $out/{} \; | sed -e "s%\./%%g" >> copy_files.sh
# now any files (again removing leading ./)
find . -type f -exec echo ifdh cp {} $out/{} \; | sed -e "s%\./%%g" >> copy_files.sh
# now take `copy_files.sh` out of the file copy script
perl -ni -e 'print if !/copy_files/' copy_files.sh
echo "file copy script contents:"
cat copy_files.sh
echo "file copy script contents:" >> $log
cat copy_files.sh >> $log
set -x
source copy_files.sh
set +x
cd ..

# example (problems with " eaten by jobsub...)
# jobsub_submit -G genie -M --OS=SL6 --resource-provides=usage_model=DEDICATED,OPPORTUNISTIC file://runGENIE.sh -p /grid/fermiapp/genie/builds/genie_R-2_9_0_buildmaster_2015-10-27/ -o /pnfs/genie/scratch/users/goran/ -c "gmkspl -p 12 -t 1000010010 -n 500 -e 500 -o scratch/pgxspl-qel.xml --event-generator-list QE"
# temporary solution: use SPACE instead of spaces
# jobsub_submit -G genie -M --OS=SL6 --resource-provides=usage_model=DEDICATED,OPPORTUNISTIC file://runGENIE.sh -p /grid/fermiapp/genie/builds/genie_R-2_9_0_buildmaster_2015-10-27/ -o /pnfs/genie/scratch/users/goran/ -c "gmksplSPACE-pSPACE12SPACE-tSPACE1000010010SPACE-nSPACE500SPACE-eSPACE500SPACE-oSPACEscratch/pgxspl-qel.xmlSPACE--event-generator-listSPACEQE"
