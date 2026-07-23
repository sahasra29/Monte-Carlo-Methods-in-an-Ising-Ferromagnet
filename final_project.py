import numpy as np
import random
import math
import matplotlib.pyplot as plt

# placeholders - change to answer questions
N = 10 #length of the square lattice
T = 1 #temperature
J = 1 #a constant that represents the strength and orientation of the interactions of spins
h = 0 #external magnetic field parameter. if not implementing optionExtension, h = 0
stabilityDeadband = 10*N**2
animationOn = True

squareLattice = np.array(np.random.choice([-1,1], size=(N,N)))
previousSquareLattice = np.copy(squareLattice)
consecutiveEqualStates = 0

def setPreviousSquareLattice():
    global squareLattice, previousSquareLattice
    previousSquareLattice = np.copy(squareLattice)

def checkStability(flipped):
    global consecutiveEqualStates, stabilityDeadband
    if flipped:
        consecutiveEqualStates = 0
    else:
        consecutiveEqualStates += 1
    if consecutiveEqualStates>=stabilityDeadband:
        return True
    else:
        return False


if animationOn:
    plt.ion()  # Turn on interactive mode
# black is representing a spin of 1, white is -1
fig, ax = plt.subplots(figsize=(6, 6))
img = ax.imshow(squareLattice, cmap='binary', vmin=-1, vmax=1)
title_text = ax.set_title("Ising Model Simulation | Step: 0", fontsize=14)
plt.title("Ising Model Simulation")
plt.axis('off')

flipped2 = False
#implement Metropolis-Hastings algorithm
for i in range(1000000):
   #choose a random point on the lattice
   if checkStability(flipped2):
       print("The Ising Model is stable at Step:",i)
       break
   current_flip = False
   r = random.randint(0,(N-1))
   c = random.randint(0,(N-1))
   energy = 4*J*squareLattice[r][c]*(squareLattice[(r+1) % N][c]+squareLattice[(r-1) % N][c]+squareLattice[r][(c+1) % N]+squareLattice[r][(c-1) % N])+squareLattice[r][c]*h
   if energy < 0:
       #if calculated energy is less than 0, flip the spin
       squareLattice[r][c] *= -1
       current_flip = True
   else:
       #if calculate energy is greater than 0, we flip the spin based on a temperature-dependent probability
       threshhold = (math.e)**(-energy/T)
       n = random.random()
       if n < threshhold:
           squareLattice[r][c] *= -1
           current_flip = True
   flipped2 = current_flip
   if animationOn:
    img.set_data(squareLattice)
    fig.canvas.draw_idle()
    plt.pause(0.0001)
   title_text.set_text(f"Ising Model Simulation | Step: {i}")

img.set_data(squareLattice)
if animationOn:
    plt.ioff()
plt.show()