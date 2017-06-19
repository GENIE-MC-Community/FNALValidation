#!/bin/bash

BUILDS=/grid/fermiapp/genie/builds/
COMPPATH=`pwd`

./compare.py --builds $BUILDS \
    --genie_tags 'R-2_12_4 R-2_12_6' \
    --genie_dates '2017-06-16 2017-06-07' \
    --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
    --comp_path ${COMPPATH}/runCompare.sh

# ./compare.py --builds $BUILDS \
#     --genie_tags 'trunk trunk' \
#     --genie_dates '2017-03-07 2017-03-20' \
#     --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
#     --comp_path ${COMPPATH}/runCompare.sh

# ./compare.py --builds $BUILDS \
#     --genie_tags 'R-2_12_4 R-2_12_2' \
#     --genie_dates '2017-03-02 2017-03-03' \
#     --top_dir /pnfs/genie/scratch/users/perdue/legacyValidation/ \
#     --comp_path ${COMPPATH}/runCompare.sh
