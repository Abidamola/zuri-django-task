import random
print('Rock, Paper, Scissors')
while True:
    print('Enter your move: R for Rock, P for Paper or S for Scissors')
    userMove = input()
    if userMove == 'R' or userMove == 'P' or userMove == 'S':
        break
    print('Enter one of R, P, or S')

if userMove == 'R':
    userChoice = 'Rock'
elif userMove == 'P':
    userChoice = 'Paper'
else: userChoice = 'Scissors'

import random
computerOption = ['Rock','Paper', 'Scissors']
randomChoice = random.choice(computerOption)



print(f"Player ({userChoice}) : Computer ({randomChoice})")

if userChoice == randomChoice :
    print("It's a tie.")
    print("Restart game.")
elif userChoice == 'Rock' and randomChoice =='Scissors':
    print('Game over!, User wins.')
elif userChoice =='Paper' and randomChoice =='Rock':
   print('Game over!, User wins.')
elif userChoice == 'Scissors' and randomChoice =='Paper':
    print('Game over!, User wins.')
elif userChoice == 'Rock' and randomChoice == 'Paper':
    print('Game over! Computer wins')
elif userChoice == 'Paper' and randomChoice == 'Scissors':
    print('Game over! Computer wins')
elif userChoice == 'Scissors' and randomChoice == 'Rock':
    print('Game over! Computer wins')