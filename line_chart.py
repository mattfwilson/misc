import matplotlib.pyplot as plt
import random


avgTemps = []
# 17, 14, 26, 41, 67, 77, 82, 86, 85, 69, 44, 32
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i in range(len(months)):
    temp = random.randint(0, 100)
    avgTemps.append(temp)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(months, avgTemps)
plt.show()