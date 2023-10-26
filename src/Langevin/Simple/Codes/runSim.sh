#!/bin/bash

rho=$1 #virus density (N/L^3)

# Edit virus density
sed -i "s/rho_[0-9]\+\.[0-9]\+/rho_${rho}/g" ../System/simple.in
# Edit msd save file name
msdName="msd_rho_${rho}"
sed -i "s/file msd.\+\.data/file ${msdName}\.data/g" ../System/simple.in
# Edit dump file name
dumpName="dump.rho_${rho}"
sed -i "46s/dump\..\+ id/${dumpName} id/" ../System/simple.in

# Run simulation
mpirun -np 4 /home/juancho/lammps-23Jun2022/src/lmp_mpi -in ../System/simple.in

# Moving generated files
mv "${msdName}.data" "../Results/${msdName}.csv"
sed -i '1,2d' ../Results/${msdName}.csv
sed -i '1s/^/step msd\n/' "../Results/${msdName}.csv"
mv ${dumpName} ../Dump/

python3 msd.py ${msdName}