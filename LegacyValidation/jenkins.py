# handle jenkins artifacts

import ast, urllib, sys, msg, os, tarfile

# url = "https://buildmaster.fnal.gov/view/GENIE/job/jenkinsTest/lastSuccessfulBuild/"
url = "https://buildmaster.fnal.gov/view/GENIE/job/buildGENIEcomparisons/lastSuccessfulBuild/"

def getBuildList(name):
  # check available artifacts at jenkins
  artifacts = []
  # url/api/python['artifacts'] returns the list of dictionaries for artifacts, we just need files names
  jsonstr = urllib.urlopen( url + "/api/python" ).read()
  for artifact in ast.literal_eval ( jsonstr )['artifacts']:
    if name in artifact['fileName']: artifacts.append (artifact['fileName'])
  return artifacts  

def getTagList (name,tag):
  # check available artifacts with given tag at jenkins
  artifacts = []
  # url/api/python['artifacts'] returns the list of dictionaries for artifacts, we just need files names
  for artifact in ast.literal_eval (urllib.urlopen(url + "/api/python").read())['artifacts']:
    if name in artifact['fileName']:
       if tag in artifact['fileName']: artifacts.append (artifact['fileName'])
  return artifacts 
  
def findLast (name,tag):
  # find the most recent build for given tag
  if getTagList(name,tag): return sorted(getTagList(name,tag))[-1][-14:-4]
  else: return "[no build for " + name + "and" + tag + "]"
  
def getBuild (name, tag, date, path):
  # get build with defined tag and date and save in path 
  buildName = name + "_" + tag + "_buildmaster_" + date
  # check if build aready exists
  if os.path.isdir (path + "/" + buildName):
    msg.warning (path + "/" + buildName + " already exists ... " + msg.BOLD + "skipping jenkins:getBuild\n", 1)
    return buildName
  # no build
  tarball = buildName + ".tgz"
  # check it build available
  if tarball not in getBuildList(name):
    msg.error ("There is no artifact for " + msg.BOLD + tarball + "\n")
    print "Available artifacts:\n"
    for artifact in getBuildList(name): print "\t" + artifact + "\n"
    sys.exit (1)
  # download build
  msg.info ("Downloading " + msg.BOLD + tarball)
  urllib.urlretrieve (url + "/artifact/genie_builds/" + tarball, path + "/" + tarball)
  # extract the build
  msg.info ("Extracting to " + msg.BOLD + path + "/" + buildName + "\n")
  tarfile.open(path + "/" + tarball, 'r').extractall(path + "/" + buildName)

  return buildName
