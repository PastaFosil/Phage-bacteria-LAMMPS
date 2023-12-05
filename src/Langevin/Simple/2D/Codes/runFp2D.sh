#!/bin/bash

dt = 0.00001 # integration step

declare -A msdFp

c=1

for j in {20..120..10}; do
    msdFp[0]=$j
    for i in $(seq 0.2 0.1 0.8); do    
        msdFp[${c}]=$(bash runSim2D.sh $i $j)
        c=$((c+1))
        if [ ${c} == 7 ]
        then
            c=1
        fi
    done
    echo ${msdFp[@]} >> Deff-Pe.csv
done