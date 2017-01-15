#!/usr/bin/env python3

# This program is used to update a lattice of random spins using the Metropolis Algorithm.
# As each spins is updated, an image of the new lattice is saved to a directory on my computer.
# These images will be used in a bash script in order to generate a gif of the lattice updating.


# The equations used to update the lattice are stored in a module called "Equations".
import Equations as eq
import numpy as np
import matplotlib.pyplot as plt

# N specifies the program to generate a lattice of NxN spins.
N = 16

# Generates a 2D lattice of random spins.
lattice = np.random.choice([-1, 1], size=(N, N))

# Temperature (in units of J/K_b)
temperature = 0.1

t = 0

while t <= 10000:
   plt.figure()
   plt.imshow(lattice, cmap='gray', vmin=-1, vmax=1, interpolation='none')
   plt.savefig("Documents/Ising_Model_Pictures/Ising_Model" + str(t) + ".png", bbox_inches='tight')
   plt.close()
   lattice = eq.Update_Lattice(lattice, temperature)
   t += 1