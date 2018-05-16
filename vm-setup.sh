#!/usr/bin/env bash

# Install method:
#
# sudo apt-get install -y curl
# curl -o vm-setup.sh https://raw.githubusercontent.com/hallgrimur1471/programming/master/vm-setup.sh
# sudo chmod +x vm-setup.sh
# ./vm-setup.sh

# replace string in file
replace() {
  local file="$1"
  local old_string="$2"
  local new_string="$3"

  cat "$file" \
      | sed 's,'"${old_string}"','"${new_string}"',g' \
      | sudo tee "$file" > /dev/null
}

# first ask a few questions
echo "Do you want to change hostname? [y/n]"
read change_hostname
if [[ "$change_hostname" == "y" ]]; then
  echo "Enter new hostname:"
  read new_hostname
fi
echo "Do you want to set up git user and email configs? [y/n]"
read configure_git
if [[ "$configure_git" == "y" ]]; then
  printf "Set username to hallgrimur1471 and email to "
  printf "hallgrimur@svarmi.com? [y/n]\n"
  read use_hallgrimur_config
  if [[ "$use_hallgrimur_config" == "y" ]]; then
    git_username="hallgrimur1471"
    git_email="hallgrimur@svarmi.com"
  else
    echo "Enter git user.name:"
    read git_username
    echo "Enter git user.email:"
    read git_email
  fi
fi

# stop on errors
set -e

# display commands
set -x

# maybe change hostname
if [[ "$change_hostname" == "y" ]]; then
  old_hostname="`hostname`"
  sudo hostname "$new_hostname"
  replace /etc/hostname "$old_hostname" "$new_hostname"
  replace /etc/hosts "$old_hostname" "$new_hostname"
  echo "Hostname changed, restart is required for changes to get through"
  echo "Restart now? [y/n]"
  read restart_now
  if [ "$restart_now" = "y" ]; then
    sudo reboot now
  fi
fi

# install stuff
sudo apt-get install -y openssh-client openssh-server
sudo apt-get install -y vim vim-gtk git
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade

# restart openssh
sudo systemctl restart ssh
sudo systemctl restart sshd

# maybe configure git
if [[ "$configure_git" == "y" ]]; then
  git config --global user.name "$git_username"
  git config --global user.email "$git_email"
  git config --global push.default simple
fi
