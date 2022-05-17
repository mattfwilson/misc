import random

bridge = []
tiles = 16
options = ['left', 'right']

for i in range(tiles):
    tile = random.choice(options)
    bridge.append(tile)

print(bridge)

for i in bridge:
    print(i)