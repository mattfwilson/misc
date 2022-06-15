import matplotlib as plt

avgTemps = [17, 14, 26, 41, 67, 77, 82, 86, 85, 69, 44, 32]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, ax = plt.subplots(figsize=(10, 6))

ax.subplot(months, avgTemps)
