import matplotlib.pyplot as plt
import numpy as np

def die_roll_experiment():
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
 
num_trials = 1000
prop = []
rolls = []
snake_eyes = 0
 
for roll in range(num_trials):
    snake_eyes += die_roll_experiment()
    prop.append(snake_eyes/(roll+1))
    rolls.append(roll+1)
 
plt.plot(rolls, prop, label='Experimental Probability')
plt.xlabel('Number of Tosses')
plt.ylabel('Percentage of Snake Eyes')

plt.hlines(0.0277, 0, num_trials, colors='red', label='True Probability of Snake Eyes')
plt.legend()

plt.show()