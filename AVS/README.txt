Automated Validation System

1. jenkins is used to build GENIE: https://buildmaster.fnal.gov/view/GENIE/job/jenkinsTest/

a) takes one argument: GENIE_VERSION (R-2_9_0 by default)
b) checks out GENIE_VERSION from svn and compiles it
c) makes a tarball: genie_GENIE_VERSION_buildmaster_YYYY-MM-DD.tgz
d) excludes ".*" and "src" from the tarball
e) creates an artifact for the build
f) logs are stored in build_logs dir (not included in the artifact)

2. getGenieFromJenkins.sh

a) gets an artifact from buildmaster
b) can get all available builds, specific build (version and/or date), or just takes the most recent build
c) one can list available builds in buildmaster
d) also sets up env vars: GENIE_BUILDS=/grid/fermiapp/genie/builds and LAST_GENIE_BUILD

3. submitGENIE.sh

a) run any script on a grid
b) one can define if job should be submitted as fermilab or as genie (default); /pnfs area is set up accordingly
c) one can define if job should be submitted onsite, offsite or both (default)
d) one can pass command line arguments to script which will be run

4. setupGENIE.sh

a) requires one argument = LAST_GENIE_BUILD
b) sets up all env variables etc

5. generateSplines.sh

a) requires the following arguments: incoming particle, target and build
b) generates a splines: splines/particle_'$particle'_target_'$target'_'$build'.xml'
c) copies output to proper /pnfs folder

6. updateBuilds.sh is a test script to run by cron

a) takes build from jenkins using getGenieFromJenkins.sh
b) extracts and removes the tarball
c) waits 12h to be sure /cvmfs is sync with /grid
d) runs some generateSplines using submitGENIE


