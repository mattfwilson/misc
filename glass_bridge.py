import random

bridge = []
bridge2 = []
tiles = 0
tiles2 = 16
options = ['left', 'right']

while tiles < 16:
    tile = random.randint(0, 1)
    bridge.append(tile)
    tiles += 1
    print(bridge)


for i in range(tiles2):
    tile = random.choice(options)
    bridge2.append(tile)
    print(bridge2)