#!/bin/bash

phi=$1 #virus density (N/L^3)

# Edit virus density
sed -i "s/phi_[0-9]\+\.[0-9]\+/phi_${phi}/g" ../System/simple2D.in
# Edit msd save file name
msdName="msd_brownian_phi_${phi}_2D"
sed -i "s/file msd.\+\.data/file ${msdName}\.data/g" ../System/simple2D.in
# Edit dump file name
dumpName="dump.brownian_phi_${phi}_2D"
sed -i "s/dump\..\+ id/${dumpName} id/" ../System/simple2D.in

# Run simulation
mpirun -np 6 /home/juancho/lammps-23Jun2022/src/lmp_mpi -in ../System/simple2D.in

# Moving generated files
mv "${msdName}.data" "../Results/${msdName}.csv"
sed -i '1,2d' ../Results/${msdName}.csv
sed -i '1s/^/step msd\n/' "../Results/${msdName}.csv"
mv ${dumpName} ../Dump/

python3 msd2D.py ${msdName}