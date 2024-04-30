import random 

# Get user input
player_choice = int(input("choose from options:\n0.snake\n1.water\n2.gun\n"))

# Determine user's choice
if player_choice == 0:
    print('you chose snake')
elif player_choice == 1:
    print('you chose water')
else:
    print('you chose gun')

# Determine computer's choice
computer_choice = [0, 1, 2]
computer = random.choice(computer_choice)
if computer == 0:
    print('computer chose snake')
elif computer == 1:
    print('computer chose water')
else:
    print('computer chose gun')

#Determine the winner

#          0 1 2
#        0 D L W 
#        1 W D L
#        2 L W D

# Total_outcomes = [[0,0][0,1][0,2][1,0][1,1][1,2][2,0][2,1][2,2]]

Win = [[0,1],[1,2],[2,0]]
Draw = [[0,0],[2,2],[3,3]]
Lose = [[1,0],[2,1],[0,1]]

if [player_choice,computer] in Win:
    print("Congradulation YOU WIN")
elif [player_choice,computer] in Lose:
    print("YOU LOSE")
else:
    print("ITS A DRAW")