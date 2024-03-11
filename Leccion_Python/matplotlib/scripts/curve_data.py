import numpy as np


nT = 100
v = 0.01

xs = np.linspace(0, 1, 100)

with open("schrodinger_data.dat", "w") as f:
    for t in range(0, nT):
        ys = np.cos(2*np.pi*(xs - v*t))

        for x, y in zip(xs, ys):
            f.write("{}, {}, {}\n".format(x, y, 2*y))

        f.write("\n")


