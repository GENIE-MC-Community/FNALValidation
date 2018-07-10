# fill dag with T2K-like test jobs

import msg
import outputPaths
import os
import commonFunctions

# 1st attempt to generate T2K event sample (minimalistic 10K events)
#
# This ius based on $GENOR_COMPARISONS/src/scripts/Production/submit_t2k_validation_mc_jobs.pl
# (case of runnu=110)
#
# gevgen -n 10000 -p 14 -t 1000060120 -e 0,20 -r 110 --seed 12345 \
#        --cross-sections input/gxspl-vA-trunk.xml \
#        -f data/measurements/vA/t2k/t2k_nd280_numucc_2013/data_release.root,flux_numu
#

# nevents="100000"
# target="1000060120"

meta = {
'Experiment' : 'T2K',
'target' : '1000060120'
}

data_struct = {
   'numucc0pi' : { 'projectile' : '14', 'energy' : '0,20',
                   'flux' : 'data/measurements/vA/t2k/t2k_nd280_numucc_2013/data_release.root,flux_numu',
		   'releaselabel' : 't2k_nd280_numu_2015',
		   'datafiles' : ['t2k_nd280_numucc0pi_2015.xml'], # no need for leading 'data/measurements/vA/t2k/'
		   'dataclass' : 'T2KND280NuMuCC0pi2015Data',
		   'mcpredictions' : ['T2KND280NuMuCC0pi2015Prediction']
		 }
}

def fillDAG( jobsub, tag, date, paths, tunes, regretags, regredir ):
   outputPaths.expand( paths['t2k'], tunes )
   commonFunctions.fillDAG_GHEP( meta, data_struct, jobsub, tag, paths['xsec_A'], paths['t2k'], tunes )
   commonFunctions.createCmpConfigs( meta, data_struct, tag, date, paths['t2krep'], tunes, regretags )
   commonFunctions.fillDAG_cmp( meta, data_struct, jobsub, tag, date, paths['xsec_A'], paths['t2k'], paths['t2krep'], tunes, regretags, regredir )

