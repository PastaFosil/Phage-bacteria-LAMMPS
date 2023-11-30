import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

os.chdir('/home/juancho/Documents/Fagocitos/src/Langevin/Simple/3D/Codes')

rho = 0.2
fp = [5.0, 10.0, 50.0, 100.0]

for i in range(len(fp)):
    msdName = f'msd_brownian_rho_{rho}_fp_{fp[i]}_3D'


    #msdName = 'msd_brownian_rho_0.2_3D'
    msd = pd.read_csv(f'../Results/{msdName}.csv',sep=' ')
    msd['step'] *= 0.00001

    str = f'fp={fp[i]}'
    print(str)
    plt.plot(msd['step'],msd['msd'], label=str)
    m,b = np.polyfit(msd['step'], msd['msd'],1)

    plt.xlabel('time')
    plt.ylabel('msd')

    plt.text(0.05,0.95-0.10*i, f'D={m/6}', transform=plt.gca().transAxes, 
                                    fontsize=14, fontweight='bold',
                                    va='top')
    '''
    f2 = plt.figure(2)
    plt.plot(msd['step'], msd['msd']/(6*msd['step']))

    plt.xlabel('time')
    plt.ylabel('D/6t')
    plt.ylim(0,1.5)
    '''
#plt.savefig(f'../Graphs/D_6t_brownian_rho_{rho}_fp_{fp}_3D.pdf')
plt.legend(loc='lower right')
plt.show()