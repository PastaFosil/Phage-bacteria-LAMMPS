import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.getcwd()

msd = pd.read_csv(f'/home/juancho/Documents/Fagocitos/src/Langevin/Simple/Results/dump_rho_0.0098.csv',sep=' ')
msd['time'] = msd['id']

msd.iloc[:156] #slice posiciones a t=0