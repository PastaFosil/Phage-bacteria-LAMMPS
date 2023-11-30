import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

os.chdir('/home/juancho/Documents/Fagocitos/src/Langevin/Simple/2D/Codes')

phi = sys.argv[1]
fp = sys.argv[2]

#phi = 0.8
#fp = 0.0

msdName = f'msd_brownian_phi_{phi}_fp_{fp}_2D'

msd = pd.read_csv(f'../Results/{msdName}.csv',sep=' ')
msd['step'] *= 0.0001

f, ax = plt.subplots()
plt.scatter(msd['step'], msd['msd']/(4*msd['step']), s=5, c='g', label='Simulation results')
plt.axhline(y=1, color='r', label='Diffusion constant')
plt.xlabel('time')
plt.ylabel(r"$\langle(\Delta r)^2\rangle/4\delta t$")
#plt.ylim(0,1.19)
plt.legend(loc='lower right')
plt.savefig(f'../Graphs/msd_brownian_phi_{phi}_fp_{fp}_2D.jpg')
#plt.show()

plt.scatter(msd['step'], msd['msd'])
m,b = np.polyfit(msd['step'], msd['msd'],1)
plt.text(0.05,0.95, f'D={m/4}', transform=plt.gca().transAxes, 
                                fontsize=14, fontweight='bold',
                                va='top')
plt.show()