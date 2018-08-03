#!/usr/bin/env bash

# maybe display help
displayHelp() {
  printf "Usage: ./install_docker_ubuntu_16.sh\n"
  printf "Installs docker and docker-compose, designed for and tested on "
  printf "Ubuntu 16.04\n"
}
thereIsAHelpArgument() { [[($# -eq 1 && ($1 = -h || $1 = --help)) ]]; }
if thereIsAHelpArgument "$@"; then
  displayHelp
  exit 0
fi

# do not run as root
if [ "$EUID" -eq 0 ];
then
    error "This script uses \${USER} so you should not run it as root"
fi

error() {
  local msg="$1"
  (2>&1 echo "Error: ${msg}")
  exit 1
}

# stop on errors
set -e

# print commands
set -x

# add GPG keyh for official Docker repository to the system
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker repository to APT sources
rep_str="deb [arch=amd64] https://download.docker.com/linux/ubuntu "
rep_str+="$(lsb_release -cs) "
rep_str+="stable"
sudo add-apt-repository "$rep_str"

# update package database with docker packages
sudo apt-get update

# make sure you are about to install from docker repo instead of default
# ubuntu 16.04 repo:
apt-cache policy docker-ce

# install docker
sudo apt-get install -y docker-ce

# check that it's running
sleep 1
systemctl is-active --quiet docker.service
if [[ "$?" != "0" ]]; then
  error "Tried to install and start docker but docker service is not running."
fi

 configure linux so you can run docker without sudo
sudo usermod -aG docker ${USER}

# usage: get_latest_release "profile/repository"
# returns: newest release number
get_latest_release() {
  curl --silent "https://api.github.com/repos/$1/releases/latest" |
    grep '"tag_name":' |
    sed -E 's/.*"([^"]+)".*/\1/'
}

latest_version="`get_latest_release docker/compose`"
docker_compose_url="https://github.com/docker/compose/releases/download/"
docker_compose_url+="${latest_version}/docker-compose-`uname -s`-`uname -m`"
sudo curl -L "${docker_compose_url}" -o /usr/local/bin/docker-compose

# (optional) install command completion for bash
completion_url="https://raw.githubusercontent.com/docker/compose/"
completion_url+="${latest_version}/contrib/completion/bash/docker-compose"
sudo curl -L "${completion_url}" -o /etc/bash_completion.d/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

set +x
echo; echo "docker and docker-compose versions:"
docker --version
docker-compose --version

printf "\nIn order to start using docker you must re-log into your user."
printf "You were added to the docker group and you must re-login for it to "
printf "take effect.\n"
printf "To re-log run this:\nsu ${USER}\n"
