import numpy as np
import random
import math
import matplotlib.pyplot as plt
# placeholders - change to answer questions
N = 30
T = 2.5
array = np.array(np.random.choice([-1,1], size=(N,N)))
print(array)
plt.ion()  # Turn on interactive mode
# black is representing a spin of 1, white is -1
fig, ax = plt.subplots(figsize=(6, 6))
img = ax.imshow(array, cmap='binary', vmin=-1, vmax=1)
title_text = ax.set_title("Ising Model Simulation | Step: 0", fontsize=14)
plt.title("Ising Model Simulation")
plt.axis('off')

for i in range(10000):
    r = random.randint(0,(N-1))
    c = random.randint(0,(N-1))
    energy = 4*array[r][c]*(array[(r+1) % N][c]+array[(r-1) % N][c]+array[r][(c+1) % N]+array[r][(c-1) % N])
    if energy < 0:
        array[r][c] *= -1
    else:
        threshhold = (math.e)**(-energy/T)
        n = random.random()
        if n < threshhold:
            array[r][c] *= -1
    img.set_data(array)
    title_text.set_text(f"Ising Model Simulation | Step: {i}")
    fig.canvas.draw_idle()
    plt.pause(0.01)

plt.ioff()
plt.show()