import random

ACTUAL_BRIDGE = []
USER_BRIDGE = []
GUESS_NUM = 0
TILES = 16
OPTIONS = ['left', 'right']

for tile in range(TILES):
    actual_tiles = random.choice(OPTIONS)
    ACTUAL_BRIDGE.append(actual_tiles)

while GUESS_NUM < 17:
    guess = input(f'What is your guess? ')
    USER_BRIDGE.append(guess)
    if USER_BRIDGE[GUESS_NUM] == ACTUAL_BRIDGE[GUESS_NUM]:
        print(f'{guess} tile is safe!')
        print(f'User bridge :{USER_BRIDGE}')
        print(f'Real bridge: {ACTUAL_BRIDGE}')
        print(USER_BRIDGE[GUESS_NUM])
    elif USER_BRIDGE[GUESS_NUM] != ACTUAL_BRIDGE[GUESS_NUM]:
        print(f'Uh oh {guess} tile broke... you ded!')
        print(f'User bridge :{USER_BRIDGE}')
        print(f'Real bridge: {ACTUAL_BRIDGE}')
        print(USER_BRIDGE[GUESS_NUM])

