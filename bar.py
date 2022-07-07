BAR = '='
PROGRESS = 100
SPACE = 0
AMOUNT = 0

while True:
    print(f'\nHP: {PROGRESS}/100')
    print('[ ' + BAR * PROGRESS + SPACE * ' ' + ' ]')
    move = input('\nAdd or subtract from bar? ')

    if move == "Add":
        AMOUNT = int(input('Add how much: '))
        total = AMOUNT + PROGRESS
        if total > 100:
            print(f'Adding {AMOUNT} would exceed your max HP!')
        else:
            PROGRESS += AMOUNT
            SPACE -= AMOUNT
    elif move == "Sub":
        AMOUNT = int(input('Subtract how much: '))
        total = PROGRESS - AMOUNT
        if total <= 0:
            print(f'Subtracting {AMOUNT} would deplete your HP to 0!')
        else:
            PROGRESS -= AMOUNT
            SPACE += AMOUNT