# fill dag with MiniBooNE-like test jobs

import msg
import outputPaths
import os
import commonFunctions

# 1st attempt to generate MiniBooNE event sample(s) (minimalistic 10K events 
#
# numu CCQE, Release-2010
#
# gevgen -n 10000 -p 14 -t 1000060120[0.857142],1000010010[0.142857] \
#        -e 0,10. --cross-sections gxspl-vA-trunk.xml -r 10000 \
#        -f data/fluxes/miniboone/miniboone_april07_baseline_rgen610.6_flux_pospolarity_fluxes.root,flux_pos_pol_numu 
#
# numubar CCQE, Release-2013
# gevgen -n 10000 -p -14 -t 1000060120[0.857142],1000010010[0.142857] \ 
# -e 0,10. --cross-sections gxspl-vA-trunk.xml -r 20000 \
 # -f data/fluxes/miniboone/miniboone_december2007_horn-174ka_rgen610.6_flux_negpolarity_fluxes.root,flux_neg_pol_numu
#
# NOTE: one may also want to use --seed <SEED>
#

# nevents="100000"

meta = {
'Experiment' : 'MiniBooNE',
'target' : '1000060120[0.857142],1000010010[0.142857]'
}

data_struct = {
   'numuccqe' : { 'projectile' : '14', 'energy' : '0,10.', 
                  'flux' : 'data/fluxes/miniboone/miniboone_april07_baseline_rgen610.6_flux_pospolarity_fluxes.root,flux_pos_pol_numu',
		  'releaselabel' : 'numu_ccqe_2010',
		  'datafiles' : [ 'miniboone_nuccqe_2010.xml' ], # no need for leading 'data/measurements/vA/miniboone/'
		  'dataclass' : 'MBCCQEData',
		  'mcpredictions' : [ 'MBCCQEPrediction' ]
                } #,
#   'numubarccqe' : { 'projectile' : '-14', 'energy' : '0,10.',
#                     'flux' : 'data/fluxes/miniboone/miniboone_december2007_horn-174ka_rgen610.6_flux_negpolarity_fluxes.root,flux_neg_pol_numu',
#		     'releaselabel' : 'numubar_ccqe_2013',
#		     'datafiles' : [ 'data/fluxes/miniboone/miniboone_december2007_horn-174ka_rgen610.6_flux_negpolarity_fluxes.root,flux_neg_pol_numu' ],
#		     'dataclass': 'MBCCQEData',
#		     'mcpredictions' : ['MBCCQEPrediction']
#                   }
}

def fillDAG( jobsub, tag, date, paths, tunes, regretags, regredir ):
   outputPaths.expand( paths['miniboone'], tunes )
   commonFunctions.fillDAG_GHEP( meta, data_struct, jobsub, tag, paths['xsec_A'], paths['miniboone'], tunes )
   commonFunctions.createCmpConfigs( meta, data_struct, tag, date, paths['mbrep'], tunes, regretags )
   commonFunctions.fillDAG_cmp( meta, data_struct, jobsub, tag, date, paths['xsec_A'], paths['miniboone'], paths['mbrep'], tunes, regretags, regredir )

