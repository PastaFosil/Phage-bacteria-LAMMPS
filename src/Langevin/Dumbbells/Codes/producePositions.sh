#!/bin/bash

# Define the parameters
L=20.0 #box side length (box will go from -L/2 to L/2)
rho=0.2 #virus density (N/L^3)
x0=1.0 #distance between monomers
mono_diam=1.0 #diameter of monomers
wall_diam=1.0 #diameter of wall particles
separation=0.01 #separation between molecules

boxSizeError="ERROR: Insufficient space for particles in box"

# Call the Python script with the parameters
output=$(python3 positions.py $L $rho $x0 $mono_diam $wall_diam $separation)

if [ "$output" == "$boxSizeError" ]
then
    echo "======================================"
    echo "~~~~~~~~~~~~~~~ ERROR  ~~~~~~~~~~~~~~~"
    echo "   LAS MOLECULAS NO CABEN EN LA CAJA"
    echo "======================================"
else
    sed -i "3s/[0-9]\+/${output}/" dataFormat.txt

    cat "dataFormat.txt" "../Data/brownian_L_${L}_rho_${rho}.data" > tmp && mv tmp "../Data/brownian_L_${L}_rho_${rho}.data"
fi