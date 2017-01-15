#!/usr/bin/env python3

import numpy as np

# This function is used to find the total energy of the lattice.
# The energy is calculated using periodic boundary conditions.
# The output is divided by 2 in order to avoid counting pairs of spins twice.
def Lattice_Energy(lattice):
  return -np.sum(
    lattice * np.roll(lattice, 1, axis=0) +
    lattice * np.roll(lattice, -1, axis=0) +
    lattice * np.roll(lattice, 1, axis=1) +
    lattice * np.roll(lattice, -1, axis=1))/2

# Boltzmann probability factor
def Flip_Probability(energy1, energy2, temperature):
  return np.exp((energy1 - energy2) / temperature)

# Updates 1 randomly chosen spin on the lattice.
def Update_Lattice(lattice, temperature):
    lattice_new = np.copy(lattice)
    i = np.random.randint(lattice.shape[0])
    j = np.random.randint(lattice.shape[1])
    lattice_new[i, j] *= -1
    
    current_energy = Lattice_Energy(lattice)
    new_energy = Lattice_Energy(lattice_new)
    
    if Flip_Probability(current_energy, new_energy, temperature) > np.random.random():
        return lattice_new
    else:
        return lattice

# Calculates the magnetisation of the lattice.
def Lattice_Mag(lattice):
    mag = np.sum(lattice)
    return mag 