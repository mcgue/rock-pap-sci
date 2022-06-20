# Rock, Paper, Scissors game without fancy external game libraries

# Import random module
import random

# Establish list of acceptable choices
choices = ['ROCK', 'PAPER', 'SCISSORS']

# Introduce game
print('Let\'s play Rock, Paper, Scissors.')

# Check whether instructions understood
while True:
    # Ask whether understand the game
    player_understands = input('Do you know how to play? Enter Y for Yes or N for No: ')
    # Break if do
    if player_understands.upper() == 'Y':
        break
    # Provide instructions
    print('Rock beats scissors, scissors beat paper, and paper beats rock.')

# Commence game statement
print('Let\'s go!')

# While loop to restart when get tie
while True:
    # Get user input
    player_choice = input('Please enter your choice: ')

    # Move to all uppercase
    player_choice = player_choice.upper()

    # Make sure user has input valid choice
    while player_choice not in choices:
        player_choice = input('Please enter ROCK, PAPER, or SCISSORS:')
        player_choice = player_choice.upper()

    # Generate computer choice
    computer_choice = choices[random.randint(0, 2)]

    # if no tie, leave this while loop
    if player_choice != computer_choice:
        break

    # Inform there is a tie and ask whether player wants to try again
    if player_choice == computer_choice:
        print('It is a tie!')
    player_answer = input('Try again? Enter Y or N ')

    # Break if player wants to stop
    if player_answer.upper() == 'N':
        break

# If no tie, determine winner
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

# Sign off to end game
print('Thanks for playing!')
