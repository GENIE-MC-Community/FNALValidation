# fill dag with MINERvA-like test jobs

import msg
import os


# Hydrocarbon1000010010[0.077418],1000060120[0.922582]
#
target = "01000010010[0.077418],1000060120[0.922582]"

nevents="100000"

data_struct = {
   'nu-CCQEQ2' : { 'projectile' : '14', 'energy' : '1.5,10.', 
                   'flux' : '$GENIE_COMPARISONS/data/fluxes/minerva/Release-2013/CCQEQ2/nu-flux-MINERvA.data',
		   'releaselabel' : 'numu_r2013' ,
		   'datafiles' : ['Release-2013/CCQEQ2/nu-Hydrocarbon.data'],
		   'mcprediction' : 'MINERvACCQEQ2'
		 },
   'nubar-CCQEQ2' : { 'projectile' : '-14', 'energy' : '1.5,10.',
                      'flux' : '$GENIE_COMPARISONS/data/fluxes/minerva/Release-2013/CCQEQ2/nubar-flux-MINERvA.data',
		      'releaselabel' : 'numubar_2013',
		      'datafiles' : ['Release-2013/CCQEQ2/nubar-Hydrocarbon.data'],
		      'mcprediction' : 'MINERvACCQEQ2'
                    }
}

def fillDAG( jobsub, tag, date, paths ):
   fillDAG_GHEP( jobsub, tag, paths['xsec_A'], paths['minerva'])
   createCmpConfigs( tag, date, paths['minervarep'])
   fillDAG_cmp( jobsub, tag, date, paths['xsec_A'], paths['minerva'], paths['minervarep'] )

def fillDAG_GHEP( jobsub, tag, xsec_a_path, out ):

   if eventFilesExist(out):
      msg.warning ("MINERvA test ghep files found in " + out + " ... " + msg.BOLD + "skipping minerva:fillDAG_GHEP\n", 1)
      return

   msg.info ("\tAdding MINERvA test (ghep) jobs\n")

   # in parallel mode
   jobsub.add ("<parallel>")
   # common configuration
   inputxsec = "gxspl-vA-" + tag + ".xml"
   options = " -n " + nevents + " -t " + target + " --cross-sections input/" + inputxsec 
   # loop over keys and generate gevgen command
   for key in data_struct.iterkeys():
     cmd = "gevgen " + options + " -p " + data_struct[key]['projectile'] + " -e " + data_struct[key]['energy'] + \
           " -f " + data_struct[key]['flux'] + " -o gntp." + key + "-" + data_struct[key]['releaselabel'] + ".ghep.root"
     logfile = "gevgen_" + key + ".log"
     # NOTE: FIXME - CHECK WHAT IT DOES !!!
     jobsub.addJob ( xsec_a_path + "/" + inputxsec, out, logfile, cmd )
   
   # done
   jobsub.add ("</parallel>")

def createCmpConfigs( tag, date, reportdir ):

   # start GLOBAL CMP CONFIG
   gcfg = reportdir + "/global-minerva-cfg-" + tag + "_" + date + ".xml"
   try: os.remove(gcfg)
   except OSError: pass
   gxml = open( gcfg, 'w' )
   print >>gxml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
   print >>gxml, '<config>'
   print >>gxml, '\t<experiment name="MINERvA">'
   print >>gxml, '\t\t<paths_relative_to_geniecmp_topdir> true </paths_relative_to_geniecmp_topdir>'

   # in the loop, create GSim cfg files and also put their names in the global cfg
   for key in data_struct.iterkeys():
      xmlfile = reportdir + "/gsimfile-" + tag + "-" + date + "-minerva-" + key + ".xml"
      try: os.remove(xmlfile)
      except OSError: pass
      xml = open( xmlfile, 'w' )
      print >>xml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
      print >>xml, '<genie_simulation_outputs>'
      print >>xml, '\t<model name="GENIE_' + tag + ":default:" + data_struct[key]['releaselabel'] + '">'
      print >>xml, '\t\t<evt_file format="ghep"> input/gntp.' + key + "-" + data_struct[key]['releaselabel'] + '.ghep.root </evt_file>'
      print >>xml, '\t</model>'
      print >>xml, '</genie_simulation_outputs>'
      xml.close()

      print >>gxml, '\t\t\t<comparisons>'

      for i in range( len( data_struct[key]['datafiles'] ) ):
         print >>gxml, '\t\t\t\t<spec>'
         print >>gxml, '\t\t\t\t\t<path2data> data/measurements/vA/minerva' + data_struct[key]['datafiles'][i] + ' </path2data>'
         print >>gxml, '\t\t\t\t\t<dataclass> MINERvAExData </dataclass>'
         print >>gxml, '\t\t\t\t\t<predictionclass> ' + data_struct[key]['mcprediction'] + ' </predictionclass>'
         print >>gxml, '\t\t\t\t</spec>'
      
      print >>gxml, '\t\t\t\t<genie> ' + xmlfile + ' </genie>'
      print >>gxml, '\t\t\t</comparison>'
   
   # now finish up and close global config
   print >>gxml, '\t</experiment>'
   print >>gxml, '</config>'
   gxml.close()
   
def fillDAG_cmp( jobsub, tag, date, xsec_a_path, eventdir, reportdir ):

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
   inputs = reportdir + "/" + config + " " + xsec_a_path + "/xsec-vA-" + tag + ".root " + plotfile + "/*.ghep.root"
   logfile = "gvld_general_comparison.log"
   jobsub.addJob ( inputs, reportdir, logfile, cmd )
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
