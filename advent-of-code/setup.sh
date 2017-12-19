#!/usr/bin/env bash

day_num="$1"
name="$2"

cat setup-template.py > day-${day_num}-1-${name}.py
cat setup-template.py > day-${day_num}-2-${name}.py
touch day-${day_num}-${name}.input
touch day-${day_num}-${name}.example

sudo chmod +x day-${day_num}-1-${name}.py
sudo chmod +x day-${day_num}-2-${name}.py

echo "run-when-modified.py . .py \"./day-${day_num}-1-${name}.py\
 < ./day-${day_num}-${name}.input\""
