BAR = '='
CURRENT = 100
MAX_BAR = 100
SPACER = 0
AMOUNT = 0

while True:
    print(f'\nHP: {CURRENT}/{MAX_BAR}')
    print('[' + BAR * CURRENT + SPACER * ' ' + ']')
    AMOUNT = int(input('\nAdd or subtract from bar: '))

    total = AMOUNT + CURRENT
    if total > MAX_BAR:
        print(f'Adding {AMOUNT} would exceed your max!')
    elif total <= 0:
        print(f'Subtracting {AMOUNT} would deplete your HP to 0!')
    else:
        CURRENT += AMOUNT
        if AMOUNT < 0:
            SPACER += abs(AMOUNT)
        else:
            SPACER -= abs(AMOUNT)