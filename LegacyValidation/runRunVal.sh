#!/bin/bash

TAG=trunk
TAG=R-2_10_10
VALPATH=/grid/fermiapp/genie/validation/FNALValidation/LegacyValidation
BUILDS=/grid/fermiapp/genie/builds
OUTDIR=/pnfs/genie/scratch/users/$USER/legacyValidation

python runLegacyValidation.py --genie_tag $TAG \
    --run_path $VALPATH/runGENIE.sh \
    --builds $BUILDS \
    --output $OUTDIR
