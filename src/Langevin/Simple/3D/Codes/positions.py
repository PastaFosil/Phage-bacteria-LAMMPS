from math import ceil
from random import uniform
import numpy as np
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
x0 = float(sys.argv[3]) #distance between monomers
mono_diam = float(sys.argv[4]) #diameter of monomers
separation = float(sys.argv[5]) #separation between molecules

L = float(sys.argv[1]) #box side length (box will go from -L/2 to L/2)
phi = float(sys.argv[2]) #virus density (N/L^3)
'''
L=20.0 #box side length (box will go from -L/2 to L/2)
phi=0.5 #virus density (N/L^3)
x0=0.0 #distance between monomers
mono_diam=1.0 #diameter of monomers
separation=0.01 #separation between molecules

N = int(round(6*L*L*L*phi/(np.pi*mono_diam*mono_diam*mono_diam))) #number of virus (2x number of monomers)
total_particles = N

virusPos = np.zeros((total_particles,3)) #virus position array

x = mono_diam/2           #x position of the first monomer
y = mono_diam/2           #y
z = mono_diam/2           #z

for i in np.arange(0,total_particles-1):
    
    virusPos[i,0] = x #x position of first monomer type
    virusPos[i,1] = y #y
    virusPos[i,2] = z #z
    '''
    virusPos[i+1,0] = x+x0 #x position of second monomer type
    virusPos[i+1,1] = y    #y
    virusPos[i+1,2] = z    #z
    '''
    y += mono_diam+separation #y position for next monomer
    
    if y>=L-(mono_diam/2): #when the Y line fills, changes the z position
        y = mono_diam
        z += mono_diam+separation
    if z>=L-mono_diam/2: #when the YZ plane fills, changes the x position
        x += x0+mono_diam+separation
        y = mono_diam
        z = mono_diam

if np.any(virusPos>L): #checks if there's not enough space for viruses (try changing separation distance)
    print('ERROR: Insufficient space for particles in box')

    sys,exit()
else:
    print(total_particles)

virusPos -= L/2 #translation to center box at origin

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

moleculeID = 0
with open(f'../Data/brownian_L_{L}_phi_{phi}.data','w') as f: #writes file with [Particle ID] [Molecule ID] [Type] [X] [Y] [Z]
    f.write(f'\n')
    for i, pos in enumerate(virusPos):
        f.write(f'{i+1} 1 {pos[0]:.16f} {pos[1]:.16f} {pos[2]:.16f}\n')