import random

FLIPS = 1000
OUTCOMES = ['HH', 'TT', 'HT', 'TH']
RESULTS = []

for flip in range(FLIPS):
    toss = random.choice(OUTCOMES)
    RESULTS.append(toss)

print(RESULTS)

heads_heads = RESULTS.count('HH')
HH_percent = heads_heads / FLIPS
HH_formatted = "{:.0%}".format(HH_percent)

heads_tails = RESULTS.count('HT')
HT_percent = heads_tails / FLIPS
HT_formatted = "{:.0%}".format(HT_percent)

tails_heads = RESULTS.count('TH')
TH_percent = tails_heads / FLIPS
TH_formatted = "{:.0%}".format(TH_percent)

tails_tails = RESULTS.count('TT')
TT_percent = tails_tails / FLIPS
TT_formatted = "{:.0%}".format(TT_percent)

print(f'Heads/Heads: {heads_heads} outcomes, representing probability of {HH_formatted}')
print(f'Heads/Tails: {heads_tails} outcomes, representing probability of {HT_formatted}')
print(f'Tails/Heads: {tails_heads} outcomes, representing probability of {TH_formatted}')
print(f'Tails/Tails: {tails_tails} outcomes, representing probability of {TT_formatted}')