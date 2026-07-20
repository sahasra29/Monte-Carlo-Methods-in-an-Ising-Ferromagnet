import numpy as np
import random
import math
import matplotlib.pyplot as plt


# placeholders - change to answer questions
N = 25 #length of the square lattice
T = 2.5 #temperature
J = 1 #a constant that represents the strength and orientation of the interactions of spins
h = 0 #external magnetic field parameter. if not implementing optionExtension, h = 0


squareLattice = np.array(np.random.choice([-1,1], size=(N,N)))
print(squareLattice)


plt.ion()  # Turn on interactive mode
# black is representing a spin of 1, white is -1
fig, ax = plt.subplots(figsize=(6, 6))
img = ax.imshow(squareLattice, cmap='binary', vmin=-1, vmax=1)
title_text = ax.set_title("Ising Model Simulation | Step: 0", fontsize=14)
plt.title("Ising Model Simulation")
plt.axis('off')


#implement Metropolis-Hastings algorithm
for i in range(10000):
   #choose a random point on the lattice
   r = random.randint(0,(N-1))
   c = random.randint(0,(N-1))
   energy = 4*squareLattice[r][c]*(squareLattice[(r+1) % N][c]+squareLattice[(r-1) % N][c]+squareLattice[r][(c+1) % N]+squareLattice[r][(c-1) % N]+h)
   if energy < 0:
       #if calculated energy is less than 0, flip the spin
       squareLattice[r][c] *= -1
   else:
       #if calculate energy is greater than 0, we flip the spin based on a temperature-dependent probability
       threshhold = (math.e)**(-energy/T)
       n = random.random()
       if n < threshhold:
           squareLattice[r][c] *= -1
   img.set_data(squareLattice)
   title_text.set_text(f"Ising Model Simulation | Step: {i}")
   fig.canvas.draw_idle()
   plt.pause(0.01)


plt.ioff()
plt.show()
