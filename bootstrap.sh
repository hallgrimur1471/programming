#!/usr/bin/env bash

# After an interactive prompt, this script installs stuff I want in most of
# my machines:
#
# * update software
# * change machine hostname
# * install & configure git
# * install openssh
# * install new versions of python and pip
# * set machine up for development (tmux & vim with custom setup etc)

# Install method:
# curl https://raw.githubusercontent.com/hallgrimur1471/programming/master/bootstrap.sh | bash

################################################################################
#                                  FUNCTIONS                                   #

# replace string in file
replace() {
  local file="$1"
  local old_string="$2"
  local new_string="$3"

  cat "$file" \
      | sed 's,'"${old_string}"','"${new_string}"',g' \
      | sudo tee "$file" > /dev/null
}

#                                                                              #
################################################################################

# Interative questions
echo "Do you want to change hostname? [y/n]"
read is_change_hostname
if [[ "$is_change_hostname" == "y" ]]; then
  echo "Enter new hostname:"
  read new_hostname
fi
echo "Do you want to configure git? [y/n]"
read is_configure_git
if [[ "$is_configure_git" == "y" ]]; then
  printf "Set username to hallgrimur1471 and email to "
  printf "hallgrimur@svarmi.com? [y/n]\n"
  read is_git_use_hallgrimur_config
  if [[ "$is_git_use_hallgrimur_config" == "y" ]]; then
    git_username="hallgrimur1471"
    git_email="hallgrimur@svarmi.com"
  else
    echo "Enter git user.name:"
    read git_username
    echo "Enter git user.email:"
    read git_email
  fi
fi
printf "Do you want to set this machine up for development? "
printf "(tmux & vim with configs, etc) [y/n]\n"
read is_set_up_for_development

# Stop on errors
set -e

# Display commands
set -x

# Update machine
sudo apt-get update
sudo apt-get upgrade -y

# Maybe change hostname
if [[ "$is_change_hostname" == "y" ]]; then
  old_hostname="`hostname`"
  sudo hostname "$new_hostname"
  replace /etc/hostname "$old_hostname" "$new_hostname"
  replace /etc/hosts "$old_hostname" "$new_hostname"
fi

# Install git
sudo apt-get install -y git

# Maybe configure git
if [[ "$is_configure_git" == "y" ]]; then
  git config --global user.name "$git_username"
  git config --global user.email "$git_email"
  git config --global push.default simple
fi

# Install openssh
sudo apt-get install -y \
    openssh-client \
    openssh-server
sudo systemctl restart ssh
sudo systemctl restart sshd

# Install new python & pip
sudo apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    apt-utils \
    software-properties-common # prerequisites
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-dev

# Maybe set machine up for development
if [[ "$is_set_up_for_development" == "y" ]]; then
  python3.8 -m pip install --user drvn.installer
  drvn_installer --install vim --with-drvn-configs
  drvn_installer --install tmux --with-drvn-configs
  drvn_installer --install all_python_versions
fi

# Maybe reboot
printf "Restart is required for some changes to get through, "
printf "such as change of hostname.\n"
echo "Restart now? [y/n]"
read is_restart_now
if [[ "$is_restart_now" == "y" ]]; then
  sudo reboot now
fi