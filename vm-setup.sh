#!/usr/bin/env bash

# replace string in file
replace() {
  local file="$1"
  local old_string="$2"
  local new_string="$3"

  cat "$file" \
      | sed 's,'"${old_string}"','"${new_string}"',g' \
      | sudo tee "$file" > /dev/null
}

# stop on errors
set -e

# display commands
set -x

# install stuff
sudo apt-get install openssh-client openssh-server
sudo apt-get install vim vim-gtk
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

# restart openssh
sudo systemctl restart ssh
sudo systemctl restart sshd

# maybe change hostname
echo "Do you want to change hostname? [y/n]"
read user_input
if [ "$user_input" = "y" ]; then
  echo "Enter new hostname:"
  read new_hostname
  old_hostname="`hostname`"
  sudo hostname "$new_hostname"
  replace /etc/hostname "$old_hostname" "$new_hostname"
  replace /etc/hosts "$old_hostname" "$new_hostname"
  echo "Hostname changed, restart is required for changes to get through"
fi
