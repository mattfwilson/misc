import scipy.stats as stats

x = 3
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

