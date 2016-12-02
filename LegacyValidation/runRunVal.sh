#!/bin/bash

TAG=trunk
TAG=R-2_12_2
VALPATH=/grid/fermiapp/genie/validation/FNALValidation/LegacyValidation
BUILDS=/grid/fermiapp/genie/builds
OUTDIR=/pnfs/genie/scratch/users/$USER/legacyValidation
DEBUG="--debug true"

python runLegacyValidation.py --genie_tag $TAG $DEBUG \
    --run_path $VALPATH/runGENIE.sh \
    --builds $BUILDS \
    --output $OUTDIR
