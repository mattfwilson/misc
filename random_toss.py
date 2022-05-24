import matplotlib.pyplot as plt
import numpy as np
import random

crates = 1000
prop = []
opens = []
hotdogs = 0

def open_crate():
    crate = ['Piece of Lint', 'Nipple', 'Hotdog', 'Charizard Pokemon Card', 'Blank Check', 'Half Drank Seltzer', 'Dual Nipples']
    weighted_open = random.choices(crate, weights=[7, 6, 5, 4, 3, 2, 1])

    if weighted_open == 'Hotdog':
        return 1
    else:
        return 0

for open in range(crates):
    hotdogs += open_crate()
    prop.append(hotdogs/(open+1))
    opens.append(open+1)
 
plt.plot(opens, prop, label='Experimental Probability')
plt.xlabel('Number of Opens')
plt.ylabel('Percentage of Hotdogs')

plt.hlines(0.0277, 0, crates, colors='red', label='True Probability of Hotdogs')
plt.legend()
plt.show()