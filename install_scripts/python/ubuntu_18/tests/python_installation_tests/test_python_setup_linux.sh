#!/usr/bin/env bash

# colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # no color

failed_tests=0

# cd into this scripts directory
cd "$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

function check_returncode_zero {
  local returncode="$?"
  if [[ "$returncode" == "0" ]]; then
    echo -e "${GREEN}Pass${NC}"
  else
    failed_tests=$(($failed_tests + 1))
    echo -e "${RED}Fail (terminates with returncode: ${returncode})${NC}"
  fi
}

function check_python_version {
  output="$1"
  regex=$2
  python_version="`echo $output | awk '{print $1}'`"
  if [[ "$python_version" =~ $regex ]]; then
    echo -e "${GREEN}Pass${NC}"
  else
    failed_tests=$(($failed_tests + 1))
    echo -e "${RED}Fail (output: ${output})${NC}"
  fi
}

function check_pip_version {
  output="$1"
  regex=$2
  pip_version="`echo $output | awk '{print $6}' | sed 's/)//g'`"
  if [[ "$pip_version" =~ $regex ]]; then
    echo -e "${GREEN}Success${NC}"
  else
    failed_tests=$(($failed_tests + 1))
    echo -e "${RED}Fail (output: ${output})${NC}"
  fi
}

# test pythonX --version has returncode 0
echo "TEST python --version should terminate with returncode 0"
python --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python2 --version should terminate with returncode 0"
python2 --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python3 --version should terminate with returncode 0"
python3 --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python2.7 --version should terminate with returncode 0"
python2.7 --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python3.6 --version should terminate with returncode 0"
python3.6 --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python3.7 --version should terminate with returncode 0"
python3.7 --version > /dev/null 2>&1
check_returncode_zero


# test scripts with pythonX shebang run the correct interpreter
printf "TEST scripts with python shebang run any pythonX.X.X version.\n"
printf "     Recommended for maximum compatibility with legacy systems: "
printf "python2.7.X\n"
output="`./test_python_shebang.py 2>&1`"
check_python_version "${output}" ^[0-9]+\.[0-9]+\.[0-9]+
printf "Legacy recommendation\n"
check_python_version "${output}" ^2+\.7+\.[0-9]+

printf "TEST scripts with python2 shebang should run any python2.X.X version.\n"
output="`./test_python2_shebang.py 2>&1`"
check_python_version "${output}" ^2\.[0-9]+\.[0-9]+

echo "TEST scripts with python3 shebang should run any python3.X.X version"
output="`./test_python3_shebang.py 2>&1`"
check_python_version "${output}" ^3\.[0-9]+\.[0-9]+

echo "TEST scripts with python2.7 shebang should run any python2.7.X version"
output="`./test_python2_7_shebang.py 2>&1`"
check_python_version "${output}" ^2\.7\.[0-9]+

echo "TEST scripts with python3.6 shebang should run any python3.6.X version"
output="`./test_python3_6_shebang.py 2>&1`"
check_python_version "${output}" ^3\.6\.[0-9]+

echo "TEST scripts with python3.7 shebang should run any python3.7.X version"
output="`./test_python3_7_shebang.py 2>&1`"
check_python_version "${output}" ^3\.7\.[0-9]+


# test pythonX -m pip --version has returncode 0
echo "TEST python2.7 -m pip --version should terminate with returncode 0"
python2.7 -m pip --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python3.6 -m pip --version should terminate with returncode 0"
python3.6 -m pip --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python3.7 -m pip --version should terminate with returncode 0"
python3.7 -m pip --version > /dev/null 2>&1
check_returncode_zero

echo "TEST python2.7 -m pip should correlate with any python2.7.X version"
output="`python2.7 -m pip --version 2>&1`"
check_pip_version "${output}" ^2\.7

echo "TEST python3.6 -m pip should correlate with any python3.6.X version"
output="`python3.6 -m pip --version 2>&1`"
check_pip_version "${output}" ^3\.6

echo "TEST python3.7 -m pip should correlate with any python3.7.X version"
output="`python3.7 -m pip --version 2>&1`"
check_pip_version "${output}" ^3\.7

# Print results
echo ""
if [[ "$failed_tests" -eq "0" ]]; then
  echo "All tests passed"
  exit 0
else
  if [[ "$failed_tests" -eq "1" ]]; then
    echo "${failed_tests} test failed"
  else
    echo "${failed_tests} tests failed"
  fi
  exit 1
fi
