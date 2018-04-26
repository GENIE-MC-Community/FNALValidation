import msg
import os, re, subprocess

class Jobsub:
    # handle jobsub command for runGENIE.sh in dag file  
    # TODO - need to get more clever with lifetimes for jobs...
    def __init__ (self, args, lifetime='23h'):
        """
        init a proper jobsub command for dag
        """
        # -n option is mandatory for jobsub (otherwise jobs will be run twice...)
        self.basecmd = "jobsub -n --OS=%s --resource-provides=usage_model=%s -G %s --expected-lifetime=%s file://%s -p %s -v %s -d %s" % \
                (args.os, args.resource, args.group, lifetime, args.run, args.builds+"/"+args.buildNameGE, args.builds+"/"+args.buildNameCmp, args.debug)
        # create dag file
        self.dagFile = args.paths['top'] + "/GENIE_CI_Validation-" + args.tag + \
                "-" + args.build_date + ".dag"
        # remove is the file exists
        try:
            os.remove (self.dagFile)
        except OSError:
            pass
        # open dag file tp write
        self.dag = open (self.dagFile, 'w')
        # prepare submit commands
        self.setup = "source /cvmfs/fermilab.opensciencegrid.org/products/common/etc/setups.sh; setup jobsub_client; "
        self.subdag = "jobsub_submit_dag -G " + args.group + " file://" + self.dagFile
  
    def submit(self):
        """
        close and submit dag
        """
        self.dag.close()
        msg.info ("Done with dag file. Ready to submit.\n")
        # check if run is not empty
        if os.stat(self.dagFile).st_size == 0:
            msg.warning ("Dag file: " + self.dagFile + " is empty. " + msg.RED + msg.BOLD + "NO JOBS TO RUN!!!\n")
            exit (0)
        # submit dag
        msg.info ("Submitting: " + self.dagFile + "\n")
        subprocess.Popen (self.setup + self.subdag, shell=True, executable="/bin/bash")

    def addJob (self, inputs, output, logfile, cmd, regre):
        """
        print given command with given options to dag file (input files to
        copy, path for output, logfilename, command)
        """
        # not-so-temporary solution as workaround for jobsub quotes issue (as
        # in, we can't have quotes in the command string)
        cmd = re.sub (' ', "SPACE", cmd)   
        inputs = re.sub (' ', "SPACE", inputs)
        # write full jobsub command to dag file
        if regre is None:
	   print >>self.dag, self.basecmd + \
                          " -i " + inputs + \
                          " -o " + output + \
                          " -l " + logfile + \
                          " -c " + cmd
	else:
	   regre = re.sub (" ", "SPACE", regre )
	   print >>self.dag, self.basecmd + \
                          " -i " + inputs + \
                          " -o " + output + \
                          " -l " + logfile + \
                          " -r " + regre + \
			  " -c " + cmd 
                      
    # print custom text to dag
    def add (self, text):
        print >>self.dag, text
