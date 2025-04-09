from random import randint  # Importing randint to generate random numbers

# ask the player for their choice and store it in the variable "player"
player = input('rock (r), paper (p) or scissors (s)?')

print(player, 'vs')  #Print their choice back to them

#Use randint to choose a random number between 1 and 3
chosen = randint(1,3)
print(chosen)  #Print the number

# Map the random number to rock, paper, or scissors
if(chosen == 1):
    computer = 'r'
elif(chosen == 2):
    computer = 'p'
else:
    computer = 's'

print(computer)  #display the computer's choice

#Conditionals for the result of the game
if(player == computer):
    print('DRAW!')  # Both choices are the same

elif(player == 'r' and computer == 's'):
    print('Player wins!')  # Rock beats scissors

elif(player == 'r' and computer == 'p'):
    print('Computer wins!')  # Paper beats rock

elif(player == 'p' and computer == 'r'):
    print('Player wins!')  # Paper beats rock

elif(player == 'p' and computer == 's'):
    print('Computer wins!')  # Scissors beat paper

elif(player == 's' and computer == 'p'):
    print('Player wins!')  # Scissors beat paper

elif(player == 's' and computer == 'r'):
    print('Computer wins!')  # Rock beats scissors