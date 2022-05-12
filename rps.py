import random

computer_roll = ''
player_roll = ''
throws = ['Rock', 'Scissors', 'Paper']

player_roll = input('What do you want to throw: [R] Rock, [P] Paper, or [S] Scissors? ')

def comp_roll():
    roll = random.choices(throws)
    return roll

computer_roll = comp_roll()

if player_roll == computer_roll:
    player_roll = input('Same throw, try again: [R] Rock, [P] Paper, or [S] Scissors? ')
elif player_roll == 'r' and computer_roll == "Scissors":
    print('You win!')
elif player_roll == 'r' and computer_roll == "Paper":
    print('You lose!')
elif player_roll == 'p' and computer_roll == "Scissors":
    print('You lose!')
elif player_roll == 'p' and computer_roll == "Rock":
    print('You win!')
elif player_roll == 's' and computer_roll == "Rock":
    print('You lose!')
elif player_roll == 's' and computer_roll == "Paper":
    print('You win!')
else:
    print('Hmm, weird situation you have yourself in.')