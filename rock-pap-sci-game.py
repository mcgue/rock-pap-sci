import random

# List of acceptable choices
choices = ['ROCK', 'PAPER', 'SCISSORS']

# Introduce game and get input
print('Let\'s play Rock, Paper, Scissors :)')

# While loop to restart when get tie
while True:
    player_choice = input('Please enter your choice: ')

    # Move to all uppercase
    player_choice = player_choice.upper()

    # Check guess for validity
    while player_choice not in choices:
        player_choice = input('Please enter ROCK, PAPER, or SCISSORS:')
        player_choice = player_choice.upper()
    
    computer_choice = choices[random.randint(0, 2)]

    if player_choice != computer_choice:
        break

    if player_choice == computer_choice:
        print('It is a tie!')
    player_answer = input('Try again? Enter Y or N ')
    if player_answer.upper() == 'N' or player_choice != computer_choice:
        break

if player_choice != computer_choice:
    if player_choice == 'ROCK':
        if computer_choice.upper() == 'SCISSORS':
            print('You win :(')
        else:
             print('You lose, haha')
    elif player_choice == 'PAPER':
        if computer_choice.upper() == 'ROCK':
            print('You win, unfortunately')
        else:
            print('Ha, you lose')
    elif player_choice == 'SCISSORS':
        if computer_choice.upper() == 'PAPER':
            print('You win.')
        else:
            print('You lose!')
    else:
        print('still calculating')

    # Print result
    print('I picked ' + computer_choice)
print('Thanks for playing!')
