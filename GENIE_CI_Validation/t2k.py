# fill dag with T2K-like test jobs

import msg
import outputPaths
import os

# 1st attempt to generate T2K event sample (minimalistic 10K events)
#
# This ius based on $GENOR_COMPARISONS/src/scripts/Production/submit_t2k_validation_mc_jobs.pl
# (case of runnu=110)
#
# gevgen -n 10000 -p 14 -t 1000060120 -e 0,20 -r 110 --seed 12345 \
#        --cross-sections input/gxspl-vA-trunk.xml \
#        -f data/measurements/vA/t2k/t2k_nd280_numucc_2013/data_release.root,flux_numu
#

nevents="100000"

target="1000060120"

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
   fillDAG_GHEP( jobsub, tag, paths['xsec_A'], paths['t2k'], tunes )
   createCmpConfigs( tag, date, paths['t2krep'], tunes, regretags )
   fillDAG_cmp( jobsub, tag, date, paths['xsec_A'], paths['t2k'], paths['t2krep'], tunes, regretags, regredir )

def fillDAG_GHEP( jobsub, tag, xsec_a_path, out, tunes ):

   if eventFilesExist(out, tunes):
      msg.warning ("T2K test ghep files found in " + out + " ... " + msg.BOLD + "skipping t2k:fillDAG_GHEP\n", 1)
      return

   msg.info ("\tAdding T2K test (ghep) jobs\n")

   # in parallel mode
   jobsub.add ("<parallel>")

   # common configuration
   inputxsec = "gxspl-vA-" + tag + ".xml"
   options = " -t " + target + " --cross-sections input/" + inputxsec 

   for key in data_struct.iterkeys():
     opt = options + " -n " + nevents
     cmd = "gevgen " + opt + " -p " + data_struct[key]['projectile'] + " -e " + data_struct[key]['energy'] + \
           " -f " + data_struct[key]['flux'] + " -o gntp." + key + "-" + data_struct[key]['releaselabel'] + ".ghep.root"
     logfile = "gevgen_" + key + ".log"
     # NOTE: FIXME - CHECK WHAT IT DOES !!!
     jobsub.addJob ( xsec_a_path+"/"+inputxsec, out, logfile, cmd, None )
     # same for tunes if specified
     if not ( tunes is None):
        for tn in range(len(tunes)):
	   optTune = " -t " + target + " --cross-sections input/" + tunes[tn] + "-gxspl-vA-" + tag + ".xml -n " + nevents
	   cmdTune = "gevgen " + optTune + " --tune " + tunes[tn] + " -p " + data_struct[key]['projectile'] + " -e " + data_struct[key]['energy'] + \
	             " -f " + data_struct[key]['flux'] + " -o " + tunes[tn] + "-gntp." + key + "-" + data_struct[key]['releaselabel'] + ".ghep.root"
	   jobsub.addJob( xsec_a_path+"/"+tunes[tn]+"/"+tunes[tn]+"-"+inputxsec, out+"/"+tunes[tn], tunes[tn]+"-"+logfile, cmdTune, None )

   # done
   jobsub.add ("</parallel>")

def createCmpConfigs( tag, date, reportdir, tunes, regretags ):

   for key in data_struct.iterkeys():
      gcfg = reportdir + "/cmp-" + data_struct[key]['releaselabel'] + "-" + tag + "_" + date + ".xml"
      gsim = "/gsimfile-" + data_struct[key]['releaselabel'] + "-" + tag + "_" + date + ".xml"
      gsimfile = reportdir + gsim
      try: os.remove(gcfg)
      except OSError: pass
      try: os.remove(gsimfile)
      except OSError: pass
      gxml = open( gcfg, 'w' )
      print >>gxml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
      print >>gxml, '<config>'
      print >>gxml, '\t<experiment name="T2K">'
      print >>gxml, '\t\t<paths_relative_to_geniecmp_topdir> false </paths_relative_to_geniecmp_topdir>'

      print >>gxml, '\t\t\t<comparison>'

      for i in range( len( data_struct[key]['datafiles'] ) ):
         print >>gxml, '\t\t\t\t<spec>'
         print >>gxml, '\t\t\t\t\t<path2data> data/measurements/vA/t2k/' + data_struct[key]['datafiles'][i] + ' </path2data>'
         print >>gxml, '\t\t\t\t\t<dataclass> ' + data_struct[key]['dataclass'] + ' </dataclass>'
         print >>gxml, '\t\t\t\t\t<predictionclass> ' + data_struct[key]['mcpredictions'][i] + ' </predictionclass>'
         print >>gxml, '\t\t\t\t</spec>'
      
      print >>gxml, '\t\t\t\t<genie> input' + gsim + ' </genie>'
      print >>gxml, '\t\t\t</comparison>'
      # now finish up and close global config
      print >>gxml, '\t</experiment>'
      print >>gxml, '</config>'
      gxml.close()
      
      xml = open( gsimfile, 'w' )
      print >>xml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
      print >>xml, '<genie_simulation_outputs>'
      print >>xml, '\t<model name="' + tag + '-' + date + ':default:' + data_struct[key]['releaselabel'] + '">'
      print >>xml, '\t\t<evt_file format="ghep"> input/gntp.' + key + '-' + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
      print >>xml, '\t\t<xsec_file> input/xsec-vA-' + tag + '.root </xsec_file>'
      print >>xml, '\t</model>'
      #tunes if specified
      if not (tunes is None):
         for tn in range(len(tunes)):
	    print >>xml, '\t<model name="' + tag + '-' + date + ':' + tunes[tn] + ':' + data_struct[key]['releaselabel'] + '">'
	    print >>xml, '\t\t<evt_file format="ghep"> input/' + tunes[tn] + '-gntp.' + key + "-" + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
            print >>xml, '\t\t<xsec_file> input/' + tunes[tn] + '-xsec-vA-' + tag + '.root </xsec_file>'
	    print >>xml, '\t</model>'
      # regression if specified
      if not (regretags is None):
         for rt in range(len(regretags)):
	    print >>xml, '\t<model name="' + regretags[rt] + ":default:" + data_struct[key]['releaselabel'] + '">'
	    print >>xml, '\t\t<evt_file format="ghep"> input/regre/' + regretags[rt] + '/gntp.' + key + '-' + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
            print >>xml, '\t\t<xsec_file> input/regre/'  + regretags[rt] + '/xsec-vA-' + rversion + '.root </xsec_file>'
	    print >>xml, '\t</model>'
      print >>xml, '</genie_simulation_outputs>'
      xml.close()   

def fillDAG_cmp( jobsub, tag, date, xsec_a_path, eventdir, reportdir, tunes, regretags, regredir ):

   # check if job is done already
   if resultsExist ( tag, date, reportdir ):
      msg.warning ("T2K comparisons plots found in " + reportdir + " ... " + msg.BOLD + "skipping t2k:fillDAG_cmp\n", 1)
      return

   # not done, add jobs to dag
   msg.info ("\tAdding T2K comparisons (plots) jobs\n")  
     
   # in serial mode
   jobsub.add ("<parallel>")

   inputs = reportdir + "/*.xml " + xsec_a_path + "/xsec-vA-" + tag + ".root " + eventdir + "/*.ghep.root "
   if not (tunes is None):
      for tn in range(len(tunes)):
	 inputs = " " + inputs + xsec_a_path + "/" + tunes[tn] + "/" + tunes[tn] + "-xsec-vA-" + tag + ".root " \
	           + eventdir + "/" + tunes[tn] + "/*.ghep.root "
   regre = None
   if not (regretags is None):
      regre = ""
      for rt in range(len(regretags)):
         regre = regre + regredir + "/" + regretags[rt] + "/events/t2k/*.ghep.root "

   for key in data_struct.iterkeys():
      inFile = "cmp-" + data_struct[key]['releaselabel'] + "-" + tag + "_" + date + ".xml"
      outFile = "genie_" + tag + "_" + data_struct[key]['releaselabel']
      cmd = "gvld_general_comparison --no-root-output --global-config input/" + inFile + " -o " + outFile
#      inputs = reportdir + "/*.xml " + xsec_a_path + "/xsec-vA-" + tag + ".root " + eventdir + "/*.ghep.root "
#      if not (tunes is None):
#         for tn in range(len(tunes)):
#	    inputs = " " + inputs + xsec_a_path + "/" + tunes[tn] + "/" + tunes[tn] + "-xsec-vA-" + tag + ".root " \
#	           + eventdir + "/" + tunes[tn] + "/*.ghep.root "
#      regre = None
#      if not (regretags is None):
#         regre = ""
#         for rt in range(len(regretags)):
#            regre = regre + regredir + "/" + regretags[rt] + "/events/t2k/*.ghep.root "
      logfile = data_struct[key]['releaselabel'] + ".log"
      jobsub.addJob ( inputs, reportdir, logfile, cmd, regre )

   # done
   jobsub.add ("</parallel>")

def eventFilesExist( path, tunes ):

   for key in data_struct.iterkeys():
      if "gntp." + key + "-" + data_struct[key]['releaselabel'] + ".ghep.root" not in os.listdir(path): return False
      if not (tunes is None):
         for tn in range(len(tunes)):
	    if tunes[tn] + "-gntp." + key + ".ghep.root" not in os.listdir(path+"/"+tunes[tn]): return False

   return True

def resultsExist( tag, date, path ):

  # check if given path contains all plots  
   for key in data_struct.iterkeys():
      outFile = "genie_" + tag + "_" + data_struct[key]['releaselabel'] + ".pdf"
      if outFile not in os.listdir (path): return False
   
   return True
