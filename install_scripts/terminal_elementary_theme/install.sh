#!/usr/bin/env bash

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
