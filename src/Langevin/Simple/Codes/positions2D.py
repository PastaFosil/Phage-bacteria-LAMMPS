from math import ceil
from random import uniform
import numpy as np
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sigma = 1 #Diametro de la particula
L = float(sys.argv[1]) #box side length (box will go from -L/2 to L/2)
#phi = .05 #packing fraction
phi = float(sys.argv[2]) #packing fraction
rho = 4*phi/(np.pi*sigma**2) #particle density
N = int(round(rho*L*L)) #number of virus (2x number of monomers)
#N=100
total_particles = 2*N

x0 = float(sys.argv[3]) #distance between monomers
mono_diam = float(sys.argv[4]) #diameter of monomers
wall_diam = float(sys.argv[5]) #diameter of wall particles

virusPos = np.zeros((2*N,2)) #virus position array

x = mono_diam           #x position of the first monomer
y = wall_diam+mono_diam #y

separation = float(sys.argv[6]) #separation between molecules

for i in np.arange(0,2*N-1):
    
    virusPos[i,0] = x #x position of first monomer type
    virusPos[i,1] = y #y
    
    y += mono_diam+separation #y position for next monomer
    
    if y>=L-(wall_diam+mono_diam/2): #when the Y line fills, changes the x position
        y = wall_diam+mono_diam
        x += x0+mono_diam+separation

if np.any(virusPos>L): #checks if there's not enough space for viruses (try changing separation distance)
    print('ERROR: Insufficient space for particles in box')

    sys,exit()
else:
    print(total_particles)

virusPos -= L/2 #translation to center box at origin
'''
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(virusPos[:,0], virusPos[:,1])

ax.axis([-L/2,L/2, -L/2,L/2])

ax.set_xlabel('X')
ax.set_ylabel('Y')

# Show the plot
plt.show()
'''
with open(f'../Data/brownian_L_{L}_phi_{phi}_2D.data','w') as f: #writes file with [Particle ID] [Molecule ID] [Type] [X] [Y] [Z]
    f.write(f'\n')
    for i, pos in enumerate(virusPos):
        f.write(f'{i+1} 1 {pos[0]:.16f} {pos[1]:.16f} 0\n')
