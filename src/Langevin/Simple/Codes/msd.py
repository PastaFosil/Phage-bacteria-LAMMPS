import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

os.chdir('/home/juancho/Documents/Fagocitos/src/Langevin/Simple/Codes')

#msdName = sys.argv[1]
msdName = "msd_rho_0.2"
msd = pd.read_csv(f'../Results/{msdName}.csv',sep=' ')
msd['step'] *= 0.00001
msd.plot(x='step',y='msd', legend=False)
m,b = np.polyfit(msd['step'], msd['msd'],1)
plt.text(0.05,0.95, f'D={m/6}', transform=plt.gca().transAxes, 
                                fontsize=14, fontweight='bold',
                                va='top')
plt.show()

plt.plot(msd['step'], msd['msd']/(6*msd['step']))
plt.show()