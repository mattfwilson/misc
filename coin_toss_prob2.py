import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20, 12))

FLIPS = 5000
TWO_HEADS = 0
PROB = []
RESULTS = []

def coin_toss():
    COIN1 = ['Heads', 'Tails']
    COIN2 = ['Heads', 'Tails']

    toss1 = np.random.choice(COIN1)
    toss2 = np.random.choice(COIN2)

    if toss1 == "Heads" and toss2 == "Heads":
        return 1
    else:
        return 0

for flip in range(FLIPS):
    TWO_HEADS += coin_toss()
    PROB.append(TWO_HEADS/(flip+1))
    RESULTS.append(flip+1)

plt.plot(RESULTS, PROB, label='Experimental Probability')
plt.xlabel('Number of Tosses')
plt.ylabel('Percentage of Two Heads')

plt.hlines(.25, 0, FLIPS, colors='red', label='True Probability of Two Heads')
plt.legend()
plt.show()



# print(RESULTS)

# heads_heads = RESULTS.count('HH')
# HH_percent = heads_heads / FLIPS
# HH_formatted = "{:.0%}".format(HH_percent)

# heads_tails = RESULTS.count('HT')
# HT_percent = heads_tails / FLIPS
# HT_formatted = "{:.0%}".format(HT_percent)

# tails_heads = RESULTS.count('TH')
# TH_percent = tails_heads / FLIPS
# TH_formatted = "{:.0%}".format(TH_percent)

# tails_tails = RESULTS.count('TT')
# TT_percent = tails_tails / FLIPS
# TT_formatted = "{:.0%}".format(TT_percent)

# print(f'Heads/Heads: {heads_heads} outcomes, representing probability of {HH_formatted}')
# print(f'Heads/Tails: {heads_tails} outcomes, representing probability of {HT_formatted}')
# print(f'Tails/Heads: {tails_heads} outcomes, representing probability of {TH_formatted}')
# print(f'Tails/Tails: {tails_tails} outcomes, representing probability of {TT_formatted}')