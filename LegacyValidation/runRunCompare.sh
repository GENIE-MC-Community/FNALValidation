#!/bin/bash

BUILDS=/grid/fermiapp/genie/builds/
COMPPATH=`pwd`

./compare.py --builds $BUILDS \
    --genie_tags 'R-2_12_2 R-2_12_0' \
    --genie_dates '2016-11-29 2016-10-31' \
    --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
    --comp_path ${COMPPATH}/runCompare.sh

# ./compare.py --builds $BUILDS \
#     --genie_tags 'trunk R-2_10_2' \
#     --genie_dates '2016-09-23 2016-02-22' \
#     --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
#     --comp_path ${COMPPATH}/runCompare.sh
