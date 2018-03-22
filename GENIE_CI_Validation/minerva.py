# fill dag with MINERvA-like test jobs

import msg
import os


# Hydrocarbon1000010010[0.077418],1000060120[0.922582]
#
target = "01000010010[0.077418],1000060120[0.922582]"

nevents="100000"

data_struct = {
   'nu-CCQEQ2' : { 'projectile' : '14', 'energy' : '1.5,10.', 
                   'flux' : 'data/fluxes/minerva/Release-2013/CCQEQ2/nu-flux-MINERvA.data',
		   'releaselabel' : 'numu_r2013' ,
		   'datafiles' : ['Release-2013/CCQEQ2/nu-Hydrocarbon.data'], # FIXME !!
		   'mcpredictions' : ['MINERvACCQEQ2']                         # Redo later as PAIRS (dict.)
		 },
   'nu-CoherentPi' : { 'projectile' : '14', 'energy' : '1.5,20.',
                       'flux' : 'data/fluxes/minerva/Release-2014/CoherentPion/nu-flux-MINERvA.data',
                       'releaselabel' : 'numu_r2014',
		       'datafiles' : [ 'Release-2014/CoherentPion/nu-Hydrocarbon-PionEnergy.data', 
		                       'Release-2014/CoherentPion/nu-Hydrocarbon-PionPolarAngle.data'
				     ],
		       'mcpredictions' : [ 'MINERvACoherentPionEnergy', 
		                            'MINERvACoherentPionPolarAngle' 
					 ]  
                     }, 
   'nu-CCMuProtonFS' : { 'projectile' : '14', 'energy' : '0.,100.',
                         'flux' : 'data/fluxes/minerva/Release-2015/MuProtonFS/nu-flux-MINERvA.data',
			 'releaselabel' : 'numu_r2015',
			 'datafiles' : ['Release-2015/MuProtonFS/nu-Hydrocarbon-CCMuPfsQ2P.data'],
			 'mcpredictions' : ['MINERvACCMuProtonFSQ2P']
                     }, 
   'nu-1ChgPion' : { 'projectile' : '14', 'energy' : '1.5,10.',
                     'flux' : 'data/fluxes/minerva/Release-2015/ChargedPion/nu-flux-MINERvA.data',
                     'releaselabel' : 'numu_r2015',
		     'datafiles' : [ 'Release-2015/ChargedPion/nu-Hydrocarbon-1ChgPionEnergy.data', 
		                     'Release-2015/ChargedPion/nu-Hydrocarbon-1ChgPionPolarAngle.data' 
				   ],
		     'mcpredictions' : [ 'MINERvACC1pichgEnergy', 
		                         'MINERvACC1pichgPolarAngle' 
				       ]
		   },
   'nubar-CCQEQ2' : { 'projectile' : '-14', 'energy' : '1.5,10.',
                      'flux' : 'data/fluxes/minerva/Release-2013/CCQEQ2/nubar-flux-MINERvA.data',
		      'releaselabel' : 'numubar_r2013',
		      'datafiles' : ['Release-2013/CCQEQ2/nubar-Hydrocarbon.data'],
		      'mcpredictions' : [ 'MINERvACCQEQ2' ]
                    },
   'nubar-CoherentPi' : { 'projectile' : '-14', 'energy' : '1.5,20.',
                          'flux' : 'data/fluxes/minerva/Release-2014/CoherentPion/nubar-flux-MINERvA.data',
                          'releaselabel' : 'numubar_r2014',
		          'datafiles' : [ 'Release-2014/CoherentPion/nubar-Hydrocarbon-PionEnergy.data', 
		                          'Release-2014/CoherentPion/nubar-Hydrocarbon-PionPolarAngle.data'
				        ],
		          'mcpredictions' : [ 'MINERvACoherentPionEnergy', 
		                              'MINERvACoherentPionPolarAngle' 
					    ]  
                        }, 
   'nubar-CC1Pi0' : { 'projectile' : '-14', 'energy' : '0.1,20.',
                      'flux' : 'data/fluxes/minerva/Release-2015/SinglePi0/nubar-flux-MINERvA.data',
                      'releaselabel' : 'numu_r2015',
		      'datafiles' : [ 'Release-2015/SinglePi0/nubar-Hydrocarbon-cc1pi0Momentum.data', 
		                      'Release-2015/SinglePi0/nubar-Hydrocarbon-cc1pi0PolarAngle.data' 
				    ],
		      'mcpredictions' : [ 'MINERvACC1pi0Momentum', 
		                          'MINERvACC1pi0PolarAngle' 
					]
                    }
}

def fillDAG( jobsub, tag, date, paths, regretags, regredir ):
   fillDAG_GHEP( jobsub, tag, paths['xsec_A'], paths['minerva'] )
   createCmpConfigs( tag, date, paths['minervarep'], regretags )
   fillDAG_cmp( jobsub, tag, date, paths['xsec_A'], paths['minerva'], paths['minervarep'], regretags, regredir )

def fillDAG_GHEP( jobsub, tag, xsec_a_path, out ):

   if eventFilesExist(out):
      msg.warning ("MINERvA test ghep files found in " + out + " ... " + msg.BOLD + "skipping minerva:fillDAG_GHEP\n", 1)
      return

   msg.info ("\tAdding MINERvA test (ghep) jobs\n")

   # in parallel mode
   jobsub.add ("<parallel>")
   # common configuration
   inputxsec = "gxspl-vA-" + tag + ".xml"
   options = " -t " + target + " --cross-sections input/" + inputxsec 
   # loop over keys and generate gevgen command
   for key in data_struct.iterkeys():
     opt = ""
     if key.find("CoherentPi") == -1:
        opt = options + " -n " + nevents
     else:
        opt = options + " -n 10000 --event-generator-list COH "
     cmd = "gevgen " + opt + " -p " + data_struct[key]['projectile'] + " -e " + data_struct[key]['energy'] + \
           " -f " + data_struct[key]['flux'] + " -o gntp." + key + "-" + data_struct[key]['releaselabel'] + ".ghep.root"
     logfile = "gevgen_" + key + ".log"
     # NOTE: FIXME - CHECK WHAT IT DOES !!!
     jobsub.addJob ( xsec_a_path + "/" + inputxsec, out, logfile, cmd, None )
   
   # done
   jobsub.add ("</parallel>")

def createCmpConfigs( tag, date, reportdir, regretags ):

   # start GLOBAL CMP CONFIG
   gcfg = reportdir + "/global-minerva-cfg-" + tag + "_" + date + ".xml"
   try: os.remove(gcfg)
   except OSError: pass
   gxml = open( gcfg, 'w' )
   print >>gxml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
   print >>gxml, '<config>'
   print >>gxml, '\t<experiment name="MINERvA">'
   print >>gxml, '\t\t<paths_relative_to_geniecmp_topdir> false </paths_relative_to_geniecmp_topdir>'

   # in the loop, create GSim cfg files and also put their names in the global cfg
   for key in data_struct.iterkeys():
      gsimfile = "/gsimfile-" + tag + "-" + date + "-minerva-" + key + ".xml"
      # ---> xmlfile = reportdir + "/gsimfile-" + tag + "-" + date + "-minerva-" + key + ".xml"
      xmlfile = reportdir + gsimfile
      try: os.remove(xmlfile)
      except OSError: pass
      xml = open( xmlfile, 'w' )
      print >>xml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
      print >>xml, '<genie_simulation_outputs>'
      print >>xml, '\t<model name="GENIE_' + tag + ":default:" + data_struct[key]['releaselabel'] + '">'
      print >>xml, '\t\t<evt_file format="ghep"> input/gntp.' + key + "-" + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
      print >>xml, '\t</model>'
      if not (regretags is None):
         for rt in range(len(regretags)):
	    print >>xml, '\t<model name="GENIE_' + regretags[rt] + ":default:" + data_struct[key]['releaselabel'] + '">'
	    print >>xml, '\t\t<evt_file format="ghep"> input/regre/' + regretags[rt] + '/gntp.' + key + "-" + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
	    print >>xml, '\t</model>'
      print >>xml, '</genie_simulation_outputs>'
      xml.close()

      print >>gxml, '\t\t\t<comparison>'

      for i in range( len( data_struct[key]['datafiles'] ) ):
         print >>gxml, '\t\t\t\t<spec>'
         print >>gxml, '\t\t\t\t\t<path2data> data/measurements/vA/minerva/' + data_struct[key]['datafiles'][i] + ' </path2data>'
         print >>gxml, '\t\t\t\t\t<dataclass> MINERvAExData </dataclass>'
         print >>gxml, '\t\t\t\t\t<predictionclass> ' + data_struct[key]['mcpredictions'][i] + ' </predictionclass>'
         print >>gxml, '\t\t\t\t</spec>'
      
      # ---> print >>gxml, '\t\t\t\t<genie> ' + xmlfile + ' </genie>'
      print >>gxml, '\t\t\t\t<genie> input' + gsimfile + ' </genie>'
      print >>gxml, '\t\t\t</comparison>'
   
   # now finish up and close global config
   print >>gxml, '\t</experiment>'
   print >>gxml, '</config>'
   gxml.close()
   
def fillDAG_cmp( jobsub, tag, date, xsec_a_path, eventdir, reportdir, regretags, regredir ):

   # check if job is done already
   if resultsExist ( tag, date, reportdir ):
      msg.warning ("MINERvA comparisons plots found in " + reportdir + " ... " + msg.BOLD + "skipping minerva:fillDAG_cmp\n", 1)
      return

   # not done, add jobs to dag
   msg.info ("\tAdding MINERvA comparisons (plots) jobs\n")    
   # in serial mode
   jobsub.add ("<serial>")
   config  = "global-minerva-cfg-" + tag + "_" + date + ".xml"
   plotfile = "genie_" + tag + "-minerva.pdf"
   cmd = "gvld_general_comparison --global-config input/" + config + " -o " + plotfile
   # add the command to dag
   inputs = reportdir + "/*.xml " + eventdir + "/*.ghep.root"
   logfile = "gvld_general_comparison.log"
   regre = None
   if not (regretags is None):
      regre = ""
      for rt in range(len(regretags)):
         regre = regre + regredir + "/" + regretags[rt] + "/events/minerva/*.ghep.root " 
   jobsub.addJob ( inputs, reportdir, logfile, cmd, regre )
   # done
   jobsub.add ("</serial>")

def eventFilesExist( path ):

   for key in data_struct.iterkeys():
      if "gntp." + key + ".ghep.root" not in os.listdir(path): return False
   return True

def resultsExist( tag, date, path ):

   # in principle, date is NOT needed...
   
   if "genie_" + tag + "-minerva_test.pdf" not in os.listdir(path): return False
   return True
