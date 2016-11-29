#!/bin/bash

BUILDS=/grid/fermiapp/genie/builds/
COMPPATH=`pwd`

./compare.py --builds $BUILDS \
    --genie_tags 'R-2_10_10 trunk' \
    --genie_dates '2016-09-22 2016-10-13' \
    --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
    --comp_path ${COMPPATH}/runCompare.sh

# ./compare.py --builds $BUILDS \
#     --genie_tags 'trunk R-2_10_2' \
#     --genie_dates '2016-09-23 2016-02-22' \
#     --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
#     --comp_path ${COMPPATH}/runCompare.sh
