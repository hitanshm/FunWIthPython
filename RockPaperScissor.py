#computer pick
from random import randint

compPick = "Hi"
while True:
    randomNum = randint(1, 3)
    if randomNum == 1:
        compPick = 'rock'
    elif randomNum == 2:
        compPick = 'paper'
    else:
        compPick = 'scissor'

    userPick = input("Pick 'rock', 'paper', or 'scissor' or 'Quit', which ends the game.")

    while userPick != 'rock' and userPick != 'paper' and userPick != 'scissor' and userPick != 'Quit':
        print('Please use correct value')
        userPick = input("Pick 'rock', 'paper', or 'scissor' or 'Quit', which ends the game.")

    print("User picked: " + userPick)
    print("Computer picked: " + compPick)
    if compPick == userPick:
        print("It's a draw")
    elif compPick == 'rock' and userPick == 'paper':
        print('You beat the computer')
    elif compPick == 'rock' and userPick == 'scissor':
        print('Computer won')
    elif compPick == 'paper' and userPick == 'scissor':
        print('You beat the computer')
    elif compPick == 'paper' and userPick == 'rock':
        print('Computer won')
    elif compPick == 'scissor' and userPick == 'rock':
        print('You beat the computer')
    elif compPick == 'scissor' and userPick == 'paper':
        print('Computer won')
    elif userPick == 'Quit':
        break
    else:
        print('Please use correct value')

