
import os

def prepare ( path ):
  
  # create a dictionary for output paths
  paths = {}
  paths['top'] = path
  
  # splines
  paths['xsec']   = path + "/xsec"
  paths['xsec_N'] = path + "/xsec/nuN"
  paths['xsec_A'] = path + "/xsec/nuA"
  
  # events
  paths['events']  = path + "/events"
  paths['mctest']  = path + "/events/mctest"
  # paths['reptest'] = path + "/events/repeatability"
  paths['xsecval'] = path + "/events/xsec_validation"
  paths['hadron']  = path + "/events/hadronization"
  paths['minerva'] = path + "/events/minerva"
  paths['t2k'] = path + "/events/t2k"
  paths['miniboone'] = path + "/events/miniboone"

  # reports
  paths['reports'] = path + "/reports"
  paths['sanity']  = path + "/reports/sanity_mctest"
  # paths['replog']  = path + "/reports/repeatability_test"
  paths['xseclog'] = path + "/reports/xsec_validation"
  paths['hadrep']  = path + "/reports/hadronization_test"
  paths['minervarep'] = path + "/reports/minerva"
  paths['t2krep'] = path + "/reports/t2k"
  paths['mbrep'] = path + "/reports/miniboone"

  # create all directiories
  for p in paths.values():
    if not os.path.exists (p): os.makedirs (p)

  # return paths dictionary
  return paths
  
def expand( gpath, tunes ):
   if not (tunes is None):
      for tn in range(len(tunes)):
         expath = gpath + "/" + tunes[tn]
	 if not os.path.exists(expath): os.makedirs(expath)
  
