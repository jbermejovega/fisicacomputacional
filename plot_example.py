# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:00:08 2021

@author: guill
"""

# Importamos el módulo matplotlib y numpy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# plt.style.use('./style.mplstyle.patch')
# plt.style.use('dark_background')

# Leemos datos de un fichero
data = np.loadtxt('dataset.txt') # 6000 puntos del atractor de Lorenz (6000x3)
x = data[:,0]
y = data[:,1]
z = data[:,2]

# Creamos una figura y hacemos nuestro primer plot
plt.figure()
plt.plot(x,y)

# Nueva figura, ahora con tres subplots ()
fig = plt.figure()
ax1 = plt.subplot(2,2,1)    # (#filas, #columnas, índice subplot)
plt.plot(x,y)
ax2 = plt.subplot(2,2,3)
plt.plot(x,z)
ax3 = plt.subplot(1,2,2,projection='3d')
plt.plot(x,y,z)

# Si queremos cambiar alguna gráfica, podemos acceder a esta a través de su variable
ax1.clear() # Borramos todo lo que hubiera en el subplot
ax2.clear()
ax1.plot(x,y, linestyle="dashed", linewidth=0.75, color='green')
ax2.plot(x,z, linestyle="dotted", linewidth=1.5, color='red')
ax1.grid(True)

ax1.set_ylabel("y(x)", fontsize=14, fontname="Times New Roman")
ax1.set_xlabel("x", fontsize=14, fontname="Times New Roman")
ax2.set_xlim(-20,0)
ax2.set_ylim(0,50)
ax2.set_ylabel("z(x)", fontsize=14, fontname="Times New Roman")
ax2.set_xlabel("x", fontsize=14, fontname="Times New Roman")


ax3.set_title("3D Lorenz attractor", fontsize=20, fontname="Times New Roman")

# Can we set up predetermined sizes, styles, colors, etc., for all our plots?
# See plt.rcParams.keys() to check options!

fig.tight_layout()
# plt.savefig('filename.png', dpi=300)



x = np.linspace(-5,5,50)
noise = 2*(np.random.rand(50) - 0.5)
y = 2.7*np.sin(1.3*x) + noise

fig, ax = plt.subplots(1,1)
ax.errorbar(x, y, noise, linestyle='', capsize = 3, ecolor='g',
               marker='o', markersize=4, label='Data')

from scipy import optimize
def test_func(x, a, b):
    return a * np.sin(b * x)

params, _ = optimize.curve_fit(test_func, x, y)
print(params)

ax.plot(x, test_func(x, params[0], params[1]), color='r', label='Fitted function')
ax.legend(loc='best')





