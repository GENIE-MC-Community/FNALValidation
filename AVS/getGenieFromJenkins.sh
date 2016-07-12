#!/bin/bash

export GENIE_BUILDS=/grid/fermiapp/genie/builds

url="https://buildmaster.fnal.gov/view/GENIE/job/jenkinsTest/lastSuccessfulBuild/artifact/GENIE/"
artifacts=(`curl -s -F "web=/dev/null;type=text/html" ${url} \
  | sed -e 's/<\/a>/<\/a>\n/g' \
  | sed -e 's/<a href/\n <a href/g' \
  | grep view | grep -v \/view \
  | sed -e 's/<a href=\"//' \
  | sed -e 's/\">view<\/a>//' \
  | sed -e 's/\/\*view\*\///'`)

buildExist() # check is build is available
{
  for (( k = 0; k < ${#artifacts[@]}; k++ ))
  do
    if [ "$1" == "${artifacts[$k]}" ]; then return 0; fi
  done

  return 1
}

getBuild() # getbuild genie_version build_date
{
  if [ -z $1 ] # genie_version is not specified (take the most recent build)
  then
    build="$(echo "${artifacts[*]}" | sed -e 's/\s\s*/\n/g' | sort | tail -n 1)"
    if buildExist $build
    then echo; echo "GENIE version was not specified. Getting the last build: $build"
    else echo; echo "Can not find the build."; listOfBuilds
    fi
  elif [ -z $2 ] # build_date is not specified (take the most for given version)
  then
    build="$(echo "${artifacts[*]}" | sed -e 's/\s\s*/\n/g' | sed '/'$1'/!d' | sort | tail -n 1)"
    if buildExist $build
    then echo; echo "Build date was not specified. Getting the last build for $1: $build"
    else echo; echo "Can not find the build for $1."; listOfBuilds
    fi
  else
    build="genie_$1_buildmaster_$2.tgz"
    if buildExist $build
    then echo; echo "Getting: $build"
    else echo; echo "Can not find the build: $build"; listOfBuilds
    fi
  fi

  echo; 
  
  if [ ! -f $GENIE_BUILDS/$build ] # check if the build already exists
  then
    curl -\# -O ${url}/$build
    mv $build $GENIE_BUILDS
    export LAST_GENIE_BUILD="${build%%.*}" # set up env variable so other scripts can refer to
  fi
}

getAllBuilds() # get all builds 
{
  for (( k = 0; k < ${#artifacts[@]}; k++ ))
  do
    if [ ! -f ${artifacts[$k]} ]
    then
      echo; echo "Getting: ${artifacts[$k]}"; echo
      curl -\# -O ${url}/${artifacts[$k]}
      mv ${artifacts[$k]} $GENIE_BUILDS
    fi
    
  done
}

listOfBuilds() # list of available builds
{
  echo; echo "List of available builds:"; echo

  for (( k = 0; k < ${#artifacts[@]}; k++ ))
  do
    echo "$k. ${artifacts[$k]}"; echo
  done
  
  exit 2
}

usage() # print help
{
  echo; echo "./getGenieFromJenkins [options]"; echo
  echo "-v genie_version [e.g. R-2_9_0]"
  echo "-d build_date [YYYY-MM-DD, if not defined - get the most recent one]"
  echo "-a [get all builds, no need to define -v and -d]"
  echo "-l [show list of available builds]"; echo
  exit 1
}

while getopts v:d:alh OPT
do
  case ${OPT} in
    v) # genie version, e.g. R-2_9_0
      version=$OPTARG
      ;;
    d) # build date, e.g. 2015-05-05
      date=$OPTARG
      ;;
    a) # get all builds
      all=true
      ;;
    l) # list available builds
      listOfBuilds
      ;;
    h)
      usage
      ;;
    *)
      usage
  esac
done

if [ "$all" = true ]; then getAllBuilds
else getBuild $version $date
fi
