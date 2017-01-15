#!/usr/bin/env python3

# This program is used to generate graphs of "Energy per Site vs. Temperature", 
# "Magnetisation per Site vs. Temperature", "Specific Heat vs. Temperature" 
# and "Susceptibility per Site vs. Temperature" using the 2D Ising Model.
# A value for the Curie Temperature will be extrapolated from these graphs.


# The equations used to update the lattice and calcualte the observables are stored in a module
# called "Equations".
import Equations as eq
import numpy as np
import matplotlib.pyplot as plt

# N specifies the program to generate a lattice of NxN spins.
N = 16

# Generates a 2D lattice of random spins.
lattice = np.random.choice([-1, 1], size=(N, N))

# A range of temperatures (in units of J/K_b)
T = np.linspace(1, 4, 150)

# A series of arrays used to store averaged values of observables.
Energy = np.zeros(150)
Magnetisation = np.zeros(150)
SpecificHeat = np.zeros(150)
Susceptibility = np.zeros(150)
    

# This loop is used to calculate the averaged value of observables ( <E^2>, <E>^2, <M^2>, <M>^2 )
# for a range of temperatures. These observables are then used to calculate the energy per site,
# magnetisation per site, specific heat capcity per site and the magnetic susceptibility per site.

for m in range(len(T)):
    
    # All of the observables have been set to 0. Once thermalisation conditions have been met,
    # these values will start to update.
    E = M = E2 = M2 = 0
     
    lattice = np.random.choice([-1, 1], size=(N,N))
    
    # Spins on the lattice are updated 5000 times in order to satisfy
    # thermilisation conditions.
    for i in range(5000):
        lattice = eq.Update_Lattice(lattice, T[m])
    
    # Specifies the number of iterations in the Monte Carlo loop.
    iterations = 400000
    
    # Values for energy, magnetisation, specific heat and susceptibility are generated
    # for each value of temperature. A large amount of Monte Carlo steps are used in
    # order to smooth out statistical errors.
    for j in range(iterations):
        lattice = eq.Update_Lattice(lattice, T[m])
        E += eq.Lattice_Energy(lattice)
        M += eq.Lattice_Mag(lattice)
        
        M2 += (eq.Lattice_Mag(lattice))*(eq.Lattice_Mag(lattice))
        E2 += (eq.Lattice_Energy(lattice))*(eq.Lattice_Energy(lattice))
        
        Energy[m] = E/(iterations*N*N)
        Magnetisation[m]  = M/(iterations*N*N)
        SpecificHeat[m]   = ( E2/iterations - E*E/(iterations**2) )/(N*N*T[m]*T[m])
        Susceptibility[m] = ( M2/iterations - M*M/(iterations**2) )/(N*N*T[m])

# Values obtained in the previous loop are plotted against temperature.        

plt.figure()
plt.plot(T, Energy, 'ro')
plt.title("Energy per Site vs. Temperature")
plt.xlabel(r"Temperature ($J / k_{b}$)")
plt.ylabel(r"Energy per Site ($J$)")

plt.figure()
plt.plot(T, abs(Magnetisation), 'bo')
plt.title("Magnetisation per Site vs. Temperature")
plt.xlabel(r"Temperature ($J / k_{b}$)")
plt.ylabel(r"Magnetisation per Site ($\mu$)")


plt.figure()
plt.plot(T, SpecificHeat, 'mo')
plt.title("Specific Heat Capacity per Site vs. Temperature")
plt.xlabel(r"Temperature ($J / k_{b}$)")
plt.ylabel(r"Specific Heat Capacity per Site ($J / k_{b}^{2}$)")


plt.figure()
plt.plot(T, Susceptibility, 'go')
plt.title("Magnetic Susceptibility per Site vs. Temperature")
plt.xlabel(r"Temperature ($J / k_{b}$)")
plt.ylabel(r"Magnetic Susceptibility per Site ($\mu / k_{b}$)")
plt.show()

# A value for the Curie temperature is obtained from the graph of "Specific Heat vs. Temperature".
# This is achieved by taking the corresponding temperature value from the peak of the graph.
Curie_Temp = T[SpecificHeat.argmax()]
print ("Curie Temperature =", Curie_Temp, "J/k_b")