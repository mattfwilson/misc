import matplotlib.pyplot as plt
import numpy as np

def coin_flip_experiment():
  # defining our two dies
    die1 = [1, 2, 3, 4, 5, 6]
    die2 = [1, 2, 3, 4, 5, 6]
 
  # "flipping" both coins randomly
    die1_result = np.random.choice(die1)
    die2_result = np.random.choice(die2)
 
  # checking if both die tosses are 1
    if die1_result == 1 and die2_result == 1:
        return 1
    else:
        return 0
 
num_trials = 5000
prop = []
tosses = []
snake_eyes = 0
 
for toss in range(num_trials):
    snake_eyes += coin_flip_experiment()
    prop.append(snake_eyes/(toss+1))
    tosses.append(toss+1)
 
plt.plot(tosses, prop, label='Experimental Probability')
plt.xlabel('Number of Tosses')
plt.ylabel('Percentage of Snake Eyes')

plt.hlines(0.25, 0, num_trials, colors='purple', label='True Probability')
plt.legend()

plt.show()