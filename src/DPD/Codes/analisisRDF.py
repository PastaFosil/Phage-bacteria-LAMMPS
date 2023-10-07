import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/juancho/Documents/Fagocitos/gr.csv")

f = np.empty(0)
pair = ["g11","g12","g13","g22","g23","g33"]
for i in range(1,10):
    f = np.append(f, df.plot(x="r", y=pair[i-1]))
    plt.xlabel("r")
    plt.ylabel(pair[i-1])

plt.show()

msdWater = pd.read_csv("/home/juancho/Documents/Fagocitos/msd1w.csv")
msdVirus = pd.read_csv("/home/juancho/Documents/Fagocitos/msd3w.csv")


f = plt.figure()
msdWater.plot(x="timestep",y="msd")
msdVirus.plot(x="timestep",y="msd")

plt.show()

msdWaternw = pd.read_csv("/home/juancho/Documents/Fagocitos/msd1NOWALL.csv")
msdVirusnw = pd.read_csv("/home/juancho/Documents/Fagocitos/msd3NOWALL.csv")

f = plt.figure()
msdWaternw.plot(x="timestep",y="msd")
msdVirusnw.plot(x="timestep",y="msd")

plt.show()