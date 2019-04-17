#!/usr/bin/env bash

set -e

while true; do
    echo "generating test set ..."
    ./waffle_choppers_gen.py > waffle_choppers_gen.in
    echo "calculating solutions ..."
    ./downloaded/platypus179-0000000000030590.py < waffle_choppers_gen.in > true.txt
    ./waffle_choppers.py < waffle_choppers_gen.in > try.txt
    echo "checking for wrong answers ..."
    if [[ "`diff true.txt try.txt`" != "" ]]; then
        break;
    else
        echo "no wrong answers found"
    fi
done