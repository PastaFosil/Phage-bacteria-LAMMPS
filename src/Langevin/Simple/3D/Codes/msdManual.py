import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.getcwd()

def MSD(pos0, post):
    '''
    Returns medium squared displacement
    '''
    norm = norm2(pos0, post)
    return norm.mean(0)

def norm2(v1,v2):
    '''
    Returns squared norm
    '''

    res = (v1-v2)*(v1-v2)
    return res.sum(1)

msdData = pd.read_csv(f'/home/juancho/Documents/Fagocitos/src/Langevin/Simple/3D/Dump/brownian_rho_0.2_fp_0.0_3D.csv',sep=' ')
#msdData['time'] = msdData['id']

N = len(msdData['id'].unique()) # number of particles
iterations = int(msdData.shape[0]/N)
for i in range(iterations): # order particle id within each iteration
    idx = i*N
    msdData[idx:idx+N] = msdData[idx:idx+N].sort_values(by='id')

msdData.set_index('id', inplace=True) # set id's as indexes

msd = np.zeros(iterations-1)
for i in range(1,iterations):
    p0 = msdData[['xu','yu','zu']][:N]
    idx = i*N
    #print()
    msd[i-1] = MSD(p0, msdData[['xu','yu','zu']][idx:idx+N])


x = np.arange(1,iterations)*0.1
plt.scatter(x[400:],msd[400:], s=100, c='blue', label='Manual')

mManual,bManual = np.polyfit(x, msd,1)

plt.text(0.05,0.95, f'D manual={mManual/6}', transform=plt.gca().transAxes, 
                                fontsize=14, fontweight='bold',
                                va='top')

rho = 0.2
fp = 0.0

msdName = f'msd_brownian_rho_{rho}_fp_{fp}_3D'

msd = pd.read_csv(f'../Results/{msdName}.csv',sep=' ')
msd['step'] *= 0.00001

f1 = plt.figure(1)
#msd.plot(x='step',y='msd', label='LAMMPS')
plt.scatter(msd['step'].iloc[4000000:], msd['msd'].iloc[4000000:], s=5, c='red', label='LAMMPS')
m,b = np.polyfit(msd['step'], msd['msd'],1)

plt.xlabel('time')
plt.ylabel('msd')
plt.text(0.05,0.85, f'D lammps={m/6}', transform=plt.gca().transAxes, 
                                fontsize=14, fontweight='bold',
                                va='top')

plt.show()