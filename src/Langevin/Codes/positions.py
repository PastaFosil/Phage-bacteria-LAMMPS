from math import ceil
from random import uniform
import numpy as np
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L = float(sys.argv[1]) #box side length (box will go from -L/2 to L/2)
rho = float(sys.argv[2]) #virus density (N/L^3)
N = int(round(rho*L*L*L)) #number of virus (2x number of monomers)
total_particles = N

x0 = float(sys.argv[3]) #distance between monomers
mono_diam = float(sys.argv[4]) #diameter of monomers
wall_diam = float(sys.argv[5]) #diameter of wall particles

virusPos = np.zeros((2*N,3)) #virus position array

x = mono_diam           #x position of the first monomer
y = wall_diam+mono_diam #y
z = mono_diam           #z

separation = float(sys.argv[6]) #separation between molecules

for i in np.arange(0,2*N-1,2):
    
    virusPos[i,0] = x #x position of first monomer type
    virusPos[i,1] = y #y
    virusPos[i,2] = z #z

    virusPos[i+1,0] = x+x0 #x position of second monomer type
    virusPos[i+1,1] = y    #y
    virusPos[i+1,2] = z    #z
    
    y += mono_diam+separation #y position for next monomer
    
    if y>=L-(wall_diam+mono_diam/2): #when the Y line fills, changes the z position
        y = wall_diam+mono_diam
        z += mono_diam+separation
    if z>=L-mono_diam/2: #when the YZ plane fills, changes the x position
        x += x0+mono_diam+separation
        y = wall_diam+mono_diam
        z = mono_diam
    
if np.any(virusPos>L): #checks if there's not enough space for viruses (try changing separation distance)
    print('ERROR: Insufficient space for particles in box')

    sys,exit()
else:
    print(total_particles)

virusPos -= L/2 #translation to center box at origin
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(virusPos[:,0], virusPos[:,1], virusPos[:,2])

ax.set_xlim3d([-L/2,L/2])
ax.set_ylim3d([-L/2,L/2])
ax.set_zlim3d([-L/2,L/2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
'''
moleculeID = 0
with open(f'../Data/brownian_L_{L}_rho_{rho}.data','w') as f: #writes file with [Particle ID] [Molecule ID] [Type] [X] [Y] [Z]
    f.write(f'\n')
    for i, pos in enumerate(virusPos):
        if i%2==0:
            moleculeID += 1
        f.write(f'{i+1} {moleculeID} 1 {pos[0]:.16f} {pos[1]:.16f} {pos[2]:.16f}\n')