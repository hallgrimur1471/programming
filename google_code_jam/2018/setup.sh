#!/usr/bin/env bash

if [ $# -eq 1 ] && [ $1 = "-h" -o $1 = "--help" ] || [ $# -eq 0 ]
then
  printf "Usage: ./setup.sh CONTEST_PART PROBLEM_CHAR\n"
  printf "Example: ./setup.sh qualification b\n"
  exit 0
fi

contest_part="$1"
problem_char="$2"

this_scripts_directory="` cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd `"
cd $this_scripts_directory

challenge_file="${contest_part}/${problem_char}.py"
cp ./template.py ./"${challenge_file}"
sudo chmod +x ./"${challenge_file}"

#challenge_set_num="$1"
#challenge_num="$2"
#challenge_name="$3"
#
#this_scripts_directory="` cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd `"
#cd $this_scripts_directory
#
#challenge_set_folder=`ls -d */ | grep "s${challenge_set_num}"\
#                      | awk '{print $1}' | sed 's/\///g'`
#
#challenge_filename=c`printf %02d ${challenge_num}`_${challenge_name}.py
#
#cp ./template.py ${challenge_set_folder}/${challenge_filename}
#
#sudo chmod +x ${challenge_set_folder}/${challenge_filename}
