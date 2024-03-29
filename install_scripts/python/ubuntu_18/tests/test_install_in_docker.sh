#!/usr/bin/env bash

# maybe display help
displayHelp() {
  printf "Usage: . ./test_install_python_ubuntu_18.sh\n"
  printf "Builds a ubuntu16.04 docker container that installs python with the "
  printf "'install_python_ubuntu_18.sh' script. After the container has been "
  printf "built a python installation test is run in the container, you will "
  printf "see the output from the test if you run this script.\n"
}
thereIsAHelpArgument() { [[($# -eq 1 && ($1 = -h || $1 = --help)) ]]; }
if thereIsAHelpArgument "$@"; then
  displayHelp
  exit 0
fi

error() {
  local msg="$1"
  (2>&1 echo "Error: ${msg}")
  exit 1
}

# root will be the "install_python_ubuntu_18" directory
root="`dirname \"$0\"`"
root="`dirname \"$root\"`"

# make sure that docker is installed
docker --version > /dev/null 2>&1
if [[ "$?" != "0" ]]; then
  error "docker is not installed (at least not on \$PATH)"
else
  # check that we have a docker version >= 18.03
  # lower versions might work but 18.03 was tested to work.
  # example output from docker --version
  #     Docker version 18.03.1-ce, build 9ee9f40
  output="`docker --version 2>/dev/null`"
  compatible_version=$( \
    echo "$output" \
    | awk '{print $3}' `# returns version number` \
    | awk -F '.' \
\ \ \ 'BEGIN {passes="true"}'\
\ \ \ '$1 < 18 {passes="false"}'\
\ \ \ '$2 < 03 {passes="false"}'\
\ \ \ 'END {print passes}') # checks if version number is high enough
  if [[ "$compatible_version" == "false" ]]; then
    error "Your docker --version must be >= 18.03"
  fi
fi

# make sure that docker-compose is installed
docker-compose --version > /dev/null 2>&1
if [[ "$?" != "0" ]]; then
  error "docker-compose is not installed (at least not on \$PATH)"
else
  # check that we have docker-compose version >= 1.18
  # lower version might work but 1.18 was tested to work.
  # example output from docker-compose --version
  #     docker-compose version 1.18.0, build 8dd22a9
  output="`docker-compose --version 2>/dev/null`"
  compatible_version=$( \
    echo "$output" \
    | awk '{print $3}' `# returns version number` \
    | awk -F '.' \
\ \ \ 'BEGIN {passes="true"}'\
\ \ \ '$1 < 1 {passes="false"}'\
\ \ \ '$2 < 18 {passes="false"}'\
\ \ \ 'END {print passes}') # checks if version number is high enough
  if [[ "$compatible_version" == "false" ]]; then
    error "Your docker-compose --version must be >= 1.18"
  fi
fi

# build the container
docker build -t python_installation_script_tester "$root"
if [[ "$?" != 0 ]]; then
  echo ""
  error "docker build failed, aborting 'test_install_python_ubuntu_18.sh'"
fi

# test the python installation by running the container
docker run python_installation_script_tester
