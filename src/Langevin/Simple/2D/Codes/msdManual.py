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

msdData = pd.read_csv(f'/home/juancho/Documents/Fagocitos/src/Langevin/Simple/Dump/msd_brownian_phi_0.8_fp_0.0_2D.csv',sep=' ')
msdData['time'] = msdData['id']

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
plt.plot(x,msd)

m,b = np.polyfit(x, msd,1)
plt.text(0.05,0.95, f'D={m/6}', transform=plt.gca().transAxes, 
                                fontsize=14, fontweight='bold',
                                va='top')
plt.show()