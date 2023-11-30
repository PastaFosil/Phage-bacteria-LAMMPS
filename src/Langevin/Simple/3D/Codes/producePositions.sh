#!/bin/bash

# Define the parameters
L=20.0 #box side length (box will go from -L/2 to L/2)
phi=$1 #virus density (N/L^3)
x0=0.0 #distance between monomers
mono_diam=1.0 #diameter of monomers
separation=0.01 #separation between molecules

boxSizeError="ERROR: Insufficient space for particles in box"

# Call the Python script with the parameters
output=$(python3 positions.py $L $phi $x0 $mono_diam $separation)

if [ "$output" == "$boxSizeError" ]
then
    echo "======================================"
    echo "~~~~~~~~~~~~~~~ ERROR  ~~~~~~~~~~~~~~~"
    echo "   LAS MOLECULAS NO CABEN EN LA CAJA"
    echo "======================================"
else
    sed -i "3s/[0-9]\+/${output}/" dataFormat.txt

    cat "dataFormat.txt" "../Data/brownian_L_${L}_phi_${phi}.data" > tmp && mv tmp "../Data/brownian_L_${L}_phi_${phi}.data"
fi