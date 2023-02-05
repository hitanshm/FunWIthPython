from random import randint

def showBoard(dis):
    print(' '.join(dis[0]))
    print(' '.join(dis[1]))
    print(' '.join(dis[2]))

def userPlay(remaining, dis, board):
    user_play_1 = int(input("user pick row value 0-2:"))
    while user_play_1 != 0 and user_play_1 != 1 and user_play_1 != 2:
        print("pick 0,1 or 2 please")
        user_play_1= int(input("user pick row value 0-2:"))
    user_play_2 = int(input("user pick column value 0-2:"))
    while user_play_2 != 0 and user_play_2 != 1 and user_play_2 != 2:
        print("pick 0,1 or 2 please")
        user_play_2= int(input("user pick column value 0-2:"))
    while [user_play_1, user_play_2] not in remaining:
        print("please put in a value that is not selected")
        user_play_1 = int(input("user pick row value 0-2:"))
        user_play_2 = int(input("user pick column value 0-2:"))
    remaining.remove([user_play_1, user_play_2])
    dis[user_play_1][user_play_2] = 'x'
    board[user_play_1][user_play_2] = 1

def compPlay(remaining, dis, board):
    length = len(remaining)
    if length ==0:
        print("Draw")
        exit(0)
    num = randint(0, length - 1)
    computer_row = remaining[num][0]
    computer_column = remaining[num][1]
    board[computer_row][computer_column] = -1
    dis[computer_row][computer_column] = 'o'
    remaining.remove([computer_row, computer_column])


def isWinner(board):
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != 0:
            return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2] != 0:
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2] != 0:
        return True
    return False
if __name__ == "__main__":
    print("you are x and computer is o")
    noWinner=True
    board= [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    remaining = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 0:
                remaining.append([i,j])
    dis=[["_","_","_"],["_","_","_"],["_","_","_"]]

    while noWinner:
        userPlay(remaining, dis, board)
        if isWinner(board):
            showBoard(dis)
            print("you win!")
            exit(0)
        compPlay(remaining, dis, board)
        if isWinner(board):
            showBoard(dis)
            print("you lose")
            exit(0)
        showBoard(dis)