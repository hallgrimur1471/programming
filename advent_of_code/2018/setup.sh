#!/usr/bin/env bash

day_num="$1"
name="$2"

cat setup_template.cpp > day_${day_num}_1_${name}.cpp
cat setup_template.cpp > day_${day_num}_2_${name}.cpp
./get_input.py 2018 ${day_num} $AOC_COOKIE > day_${day_num}_${name}.input
touch day_${day_num}_${name}.example

echo "run-when-modified.py . .cpp \
  \"program=day_${day_num}_1_${name} \
  && g++ -std=c++14 \
  -o \\\${program} \
  ./\\\${program}.cpp \
  && time ./\\\${program} \
  < ./day_${day_num}_${name}.input\""
