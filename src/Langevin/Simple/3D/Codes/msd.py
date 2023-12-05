import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

os.chdir('/home/juancho/Documents/Fagocitos/src/Langevin/Simple/3D/Codes')

#phi = sys.argv[1]
#fp = sys.argv[2]

phi = 0.2
fp = 0.0

msdName = f'msd_brownian_phi_{phi}_fp_{fp}_3D'


#msdName = 'msd_brownian_phi_0.2_3D'
msd = pd.read_csv(f'../Results/{msdName}.csv',sep=' ')
msd['step'] *= 0.00001

m,b = np.polyfit(msd['step'], msd['msd'],1)

f, ax = plt.subplots()
plt.scatter(msd['step'], msd['msd']/(6*msd['step']), s=5, c='g', label='Simulation results')
plt.axhline(y=1, color='r', label='Diffusion constant')
plt.xlabel('time')
plt.ylabel(r"$\langle(\Delta r)^2\rangle/6\delta t$")
plt.ylim(0,1.19)
plt.legend(loc='lower right')
#plt.show()
plt.savefig(f'../Graphs/msd_brownian_phi_{phi}_fp_{fp}_3D.jpg')
