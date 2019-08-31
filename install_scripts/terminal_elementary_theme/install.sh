#!/usr/bin/env bash

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  (2>&1 echo "This script must be sourced (source install.sh)")
  exit 1
fi

set -e
set -x

# Install prerequisites
sudo apt-get install -y \
  dconf-cli \
  uuid-runtime \
  wget

# Install Elementary theme
export TERMINAL=gnome-terminal
echo 38 | bash -c  "$(wget -qO- https://git.io/vQgMr)"

echo "Right click terminal -> profiles -> Elementary"
echo "Open 'properties' to make it the default profile"
