import random

# List of acceptable choices
choices = ['ROCK', 'PAPER', 'SCISSORS']

# Introduce game and get input
print('Let\'s play Rock, Paper, Scissors :)')
player_choice = input('Please enter your choice:')

# Move to all uppercase
player_choice = player_choice.upper()

# Check guess for validity
while player_choice not in choices:
    player_choice = input('Please enter ROCK, PAPER, or SCISSORS:')
    player_choice = player_choice.upper()
    
computer_choice = choices[random.randint(0,2)]

print(computer_choice)

# Print result
print(player_choice)

