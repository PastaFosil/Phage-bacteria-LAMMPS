#!/bin/bash


rho=$1

dumpName="dump.rho_${rho}"
sed -i "1s/dump\..\+ id/${dumpName} id/" testFile.txt