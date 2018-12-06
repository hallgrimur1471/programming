#!/usr/bin/env bash

day_num="$1"
name="$2"

cat setup_template.cpp > day_${day_num}_1_${name}.cpp
cat setup_template.cpp > day_${day_num}_2_${name}.cpp
./get_input.py 2018 ${day_num} $AOC_COOKIE > day_${day_num}_${name}.input
touch day_${day_num}_${name}.example

echo "run-when-modified.py . .cpp \
  \"g++ -std c++17 \
  -o day_${day_num}_1_${name} \
  ./day_${day_num}_1_${name}.cpp \
  && ./day_${day_num}_1_${name} \
  < ./day_${day_num}_${name}.input\""
