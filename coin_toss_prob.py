import random

FLIPS = 1000
OUTCOMES = ['HH', 'TT', 'HT', 'TH']
RESULTS = []

while FLIPS > 0:
    toss = random.choice(OUTCOMES)
    RESULTS.append(toss)
    FLIPS -= 1

print(RESULTS)

heads_heads = RESULTS.count('HH')
heads_tails = RESULTS.count('HT')
tails_heads = RESULTS.count('TH')
tails_tails = RESULTS.count('TT')

print(f'HH: {heads_heads}')
print(f'HT: {heads_tails}')
print(f'TH: {tails_heads}')
print(f'TT: {tails_tails}')