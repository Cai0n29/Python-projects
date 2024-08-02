import numpy as np
np.random.seed(123)
tails = [0]
for i in range(10):
    coins = np.random.randint(0,2)
    tails.append(tails[i] + coins)
print(tails)