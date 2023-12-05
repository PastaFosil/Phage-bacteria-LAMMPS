#!/bin/bash

phi=$1 # virus density (N/L^3)
fp=$2 # self-propelling force
dt=0.00001 # integration step


# Edit packing fraction and self-propelling force
sed -i "s/phi_[0-9]\+\.[0-9]\+/phi_${phi}/g" ../System/simple.in
sed -i "s/fp_[0-9]\+\.[0-9]\+/fp_${fp}/g" ../System/simple.in
# Edit msd save file name
msdName="msd_brownian_phi_${phi}_fp_${fp}_3D"
sed -i "s/file msd.\+\.data/file ${msdName}\.data/g" ../System/simple.in
# Edit dump file name
dumpName="dump.brownian_phi_${phi}_fp_${fp}_3D"
sed -i "s/dump\..\+ id/${dumpName} id/" ../System/simple.in
# Edit self-propulsion magnitude
sed -i "16s/variable fp equal [0-9]\+\.[0-9]\+/variable fp equal ${fp}/" ../System/simple.in
# Edit integration step
sed -i "26s/timestep [0-9]\+\.[0-9]\+/timestep ${dt}/" ../System/simple.in

# Run simulation
mpirun -np 3 /home/juancho/lammps-23Jun2022/src/lmp_mpi -in ../System/simple.in

# Moving generated files
mv "${msdName}.data" "../Results/${msdName}.csv"
sed -i '1,2d' ../Results/${msdName}.csv
sed -i '1s/^/step msd\n/' "../Results/${msdName}.csv"
mv ${dumpName} ../Dump/

python3 msd.py ${phi} ${fp} ${dt}

gio open ../Graphs/msd_brownian_phi_${phi}_fp_${fp}_3D.pdf