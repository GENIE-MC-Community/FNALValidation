# FNAL Validation Scripts

Recent revisions(s) can be found under "run_comparisons" branch.

Until recently (approx. mid-Oct.2018) we were able to operate  
* https://github.com/GENIEMC/FNALValidation/tree/run_comparisons/LegacyValidation

However, with ongoing changes in the FNAL grid machinery, it may be problematic; 
instead we'll rely on the genie_ci: https://cdcvs.fnal.gov/redmine/projects/genie_ci/wiki

Most current development/updates has just started (Jan.2018):
* https://github.com/GENIEMC/FNALValidation/tree/run_comparisons/GENIE_CI_Validation


Initial version was based on code by Tomasz Golan.

* https://github.com/TomaszGolan/legacyValidation
* https://github.com/TomaszGolan/genieScripts

## Example runs

    ./runLegacyValidation.py --genie_tag trunk \
        --run_path /grid/fermiapp/genie/legacyValidation/runGENIE.sh \
        --builds /grid/fermiapp/genie/builds/ \
        --output /pnfs/genie/scratch/users/$USER/legacyValidation
