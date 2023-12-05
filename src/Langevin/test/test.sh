#!/bin/bash

touch /home/juancho/Documents/Fagocitos/src/Langevin/test/arr.csv
rho=$(bash test0.sh)
declare -A arr

c=0
for i in {1..5}; do
    for j in {1..5}; do
        arr[${j}]=$(bash test0.sh ${c})
        c=$((c+1))
    done
    r=$((r+1))
    echo ${arr[@]} >> arr.csv
done
#dumpName="dump.rho_${rho}"
#sed -i "1s/dump\..\+ id/${dumpName} id/" testFile.txt