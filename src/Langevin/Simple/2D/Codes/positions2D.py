from math import ceil
from random import uniform
import numpy as np
import sys\

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x0 = float(sys.argv[3]) #distance between monomers
mono_diam = float(sys.argv[4]) #diameter of monomers
separation = float(sys.argv[5]) #separation between molecules

L = float(sys.argv[1]) #box side length (box will go from -L/2 to L/2)
#phi = .05 #packing fraction
phi = float(sys.argv[2]) #packing fraction
N = int(round(4*L*L*phi/(np.pi*mono_diam*mono_diam))) #number of virus (2x number of monomers)
#N=100
#total_particles = 2*N
total_particles = N

'''
x0 = 0.01 #distance between monomers
mono_diam = 1.0 #diameter of monomers
separation = 0.1 #separation between molecules

L = 20.0 #box side length (box will go from -L/2 to L/2)
phi = 0.05 #packing fraction
N = int(round(4*L*L*mono_diam/(np.pi*mono_diam*mono_diam))) #number of virus (2x number of monomers)
total_particles = N
print(N)
'''
virusPos = np.zeros((total_particles,2)) #virus position array

x = mono_diam           #x position of the first monomer
y = mono_diam #y

for i in np.arange(0,total_particles-1):
    
    virusPos[i,0] = x #x position of first monomer type
    #virusPos[i,1] = y #y
    
    y += mono_diam+separation #y position for next monomer
    
    if y>=L-(mono_diam/2): #when the Y line fills, changes the x position
        y = mono_diam
        x += x0+mono_diam+separation

if np.any(virusPos>L): #checks if there's not enough space for viruses (try changing separation distance)
    print('ERROR: Insufficient space for particles in box')
    #print(total_particles)
    #sys,exit()
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
