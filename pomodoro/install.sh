#!/usr/bin/env bash

set -e
set -x

pomodoro_dir=$(dirname $(readlink -f "$0"))

python3.6 -m pip install -r ${pomodoro_dir}/requirements.txt

if [ ! -f /usr/local/share/pomodoro.py ]; then
  sudo ln -s ${pomodoro_dir}/pomodoro.py /usr/local/share/pomodoro.py
fi
sudo cp pomodoro.service /etc/systemd/system/pomodoro.service
sudo systemctl enable pomodoro.service
sudo systemctl stop pomodoro.service
sudo systemctl start pomodoro.service
