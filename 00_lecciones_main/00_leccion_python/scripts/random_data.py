import random
import numpy as np

npoints = 3
nsteps = 500

xs = np.zeros((npoints, nsteps))
ys = np.zeros((npoints, nsteps))

xs[:,0] = 40*(2*np.random.random(npoints) - 1)
ys[:,0] = 40*(2*np.random.random(npoints) - 1)

for j in range(1, nsteps):
    xs[:, j] = xs[:, j-1] + 4*(2*np.random.random(npoints) - 1)
    ys[:, j] = ys[:, j-1] + 4*(2*np.random.random(npoints) - 1)


with open("posiciones_planetas.dat", "w") as f:
    for j_step in range(nsteps):
        for j_point in range(npoints):
            f.write("{}, {}\n".format(xs[j_point, j_step], ys[j_point, j_step]))

        f.write("\n")
            
    
