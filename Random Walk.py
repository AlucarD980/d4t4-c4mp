#Simulating a random walk
import numpy as np
import matplotlib.pyplot as plt

#Setting random seed
np.random.seed(123)

#Initialize random_walk
random_walk = [0]

for x in range(99):
    step = random_walk[-1]

    dice = np.random.randint(1,7)

    if dice <= step - 1:

        #Max function prevents step value going below 0
        step = max(0, step -1)
    elif dice <= 5:
        step = step +1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)


plt.plot(random_walk)
plt.ylabel('Random Walk')
plt.show()

