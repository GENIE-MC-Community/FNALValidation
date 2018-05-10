# fill dag file with neutrino-nucleus cross section splines jobs

import msg
import outputPaths
import re, os

nKnots    = "200" # no. of knots for gmkspl
maxEnergy = "150"  # maximum energy for gmkspl

nuPDG = "12,-12,14,-14" # pdg of neutrinos to process

# targets to process
targets = ['1000010010',  # H1
           '1000000010',  # n
           '1000060120',  # C12
           '1000080160',  # O16
           '1000100200',  # Ne20
           '1000130270',  # Al27
           '1000140300',  # Si30
           '1000180380',  # Ar38
           '1000260560'   # Fe56
          ];
          
def fillDAG (jobsub, tag, paths, tunes):
  outputPaths.expand( paths['xsec_A'], tunes )
  fillDAGPart (jobsub, tag, paths['xsec_N'], paths['xsec_A'], tunes)
  fillDAGMerge (jobsub, tag, paths['xsec_A'], tunes)
  
def fillDAGPart (jobsub, tag, xsec_n_path, out, tunes):
  # check if job is done already
  if isDonePart (tag, out, tunes):
    msg.warning ("Nucleus splines found in " + out + " ... " + msg.BOLD + "skipping nua:fillDAGPart\n", 1)
    return

  # not done, add jobs to dag
  msg.info ("\tAdding nucleus splines (part) jobs\n")
  # in parallel mode
  jobsub.add ("<parallel>")

  # common options
  inputFile = "gxspl-vN-" + tag + ".xml"
  inputs = xsec_n_path + "/*.xml"
  options = " --input-cross-sections input/" + inputFile
  # loop over targets and generate proper command
  for t in targets:
    outputFile = "gxspl_" + t + ".xml"
    cmd = "gmkspl -p " + nuPDG + " -t " + t + " -n " + nKnots + " -e " + maxEnergy + options + \
          " --output-cross-sections " + outputFile
    logFile = "gxspl_" + t + ".xml.log"
    jobsub.addJob (inputs, out, logFile, cmd, None)
    # same for tunes if specified
    if not (tunes is None):
       for tn in range(len(tunes)):
          inputsTune = xsec_n_path + "/" + tunes[tn] + "/*.xml"
	  optionsTune = " --input-cross-sections input/" + tunes[tn] + "-" + inputFile
	  outputTune = tunes[tn] + "-" + outputFile
	  cmdTune = "gmkspl -p " + nuPDG + " -t " + t + " -n " + nKnots + " -e " + maxEnergy + optionsTune + \
		    " --tune " + tunes[tn] + " --output-cross-sections " + outputTune
	  jobsub.addJob( inputsTune, out+"/"+tunes[tn], tunes[tn]+"-"+logFile, cmdTune, None )
          
  # done
  jobsub.add ("</parallel>")
  
def fillDAGMerge (jobsub, tag, out, tunes):
  # check if job is done already
  if isDoneMerge (tag, out, tunes):
    msg.warning ("Nucleus merged splines found in " + out + " ... " + msg.BOLD + "skipping nua:fillDAGMerge\n", 1)
    return
  # not done, add jobs to dag
  msg.info ("\tAdding nucleus splines (merge) jobs\n")

  # in serial mode
  jobsub.add ("<serial>")

  # common options
  xmlFile = "gxspl-vA-" + tag + ".xml"
  # merge splines job
  cmd = "gspladd -d input -o " + xmlFile
  inputs = out + "/gxspl*.xml"
  logFile = "gspladd.log"
  jobsub.addJob (inputs, out, logFile, cmd, None)
  # convert to root job
  rootFile = "xsec-vA-" + tag + ".root"
  cmd = "gspl2root -p " + nuPDG + " -t " + ",".join(targets) + " -o " + rootFile + " -f input/" + xmlFile
  inputs = out + "/" + xmlFile
  logFile = "gspl2root.log"
  jobsub.addJob (inputs, out, logFile, cmd, None)
  # same for tunes if specified
  if not (tunes is None):
     for tn in range(len(tunes)):
        xmlTune = tunes[tn] + "-gxspl-vA-" + tag + ".xml"
	cmdTune = "gspladd -d input -o " + xmlTune
	logTune = tunes[tn] + "-gspladd.log"
	jobsub.addJob( out+"/"+tunes[tn]+"/"+tunes[tn]+"*.xml", out+"/"+tunes[tn], logTune,cmdTune, None )
	rootTune = tunes[tn] + "-xsec-vA-" + tag + ".root"
	logTune = tunes[tn] + "-gspl2root.log"
	cmdTune = "gspl2root -p " + nuPDG + " -t " + ",".join(targets) + " -o " + rootTune + " -f input/" + xmlTune + " --tune " + tunes[tn]
	jobsub.addJob( out+"/"+tunes[tn]+"/"+xmlTune, out+"/"+tunes[tn], logTune,cmdTune, None )

  # done
  jobsub.add ("</serial>")

def isDonePart (tag, path, tunes):

  # check if given path contains all splines
  for t in targets:
    if "gxspl_" + t + ".xml" not in os.listdir (path): return False
    if not (tunes is None):
       for tn in range(len(tunes)):
          if tunes[th] +"-gxspl_" + t + ".xml" not in os.listdir (path+"/"+tunes[tn]): return False 
  
  return True

def isDoneMerge (tag, path, tunes):

  if "gxspl-vA-" + tag + ".xml" not in os.listdir (path): return False
  if "xsec-vA-" + tag + ".root" not in os.listdir (path): return False

  if not (tunes is None):
     for tn in range(len(tunes)):
        if tunes[tn] + "-gxspl-vA-" + tag + ".xml" not in os.listdir (path+"/"+tunes[tn]): return False
	if tunes[tn] + "-xsec-vA-" + tag + ".root" not in os.listdir (path+"/"+tunes[tn]): return False
  
  return True
