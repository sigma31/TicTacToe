def isMoveLeft(board):
    for i in range (0,3):
        for j in range(0,3):
            if(board[i][j] == ' '): return True
    return False

def evaluate(board):
    for row in range(0,2):
        if(board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if(board[row][0] == player):
                return -10
            elif(board[row][0] == computer):
                return 10
    for col in range(0,2):
        if(board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if(board[0][col] == player): 
                return -10
            elif(board[0][col] == computer):
                return 10
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if(board[0][0] == player):
            return -10
        elif(board[0][0] == computer):
            return 10
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if(board[0][2] == player):
            return -10
        elif(board[0][2] == computer):
            return 10
    return 0

def minmax(board,depth,isMax):
    score = evaluate(board)
    if(score == 10):
        return score-depth
    if(score == -10):
        return score+depth
    if(isMoveLeft(board) == False):
        return 0
    if(isMax):
        best = -1000
        for i in range (0,3):
            for j in range (0,3):
                if(board[i][j] == ' '):
                    board[i][j] = computer
                    best = max(best,minmax(board,depth+1,not isMax))
                    board[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j] == ' '):
                    board[i][j] = player
                    best = min(best,minmax(board,depth+1,not isMax))
                    board[i][j] = ' '
        return best
                
def findBestMove(board):
    bestMove = (-1,-1)
    bestValue = -1000
    
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] == ' '):
                board[i][j] = computer
                moveVal =  minmax(board,0,False)
                board[i][j] = ' '
                if(moveVal > bestValue):
                    bestValue = moveVal
                    bestMove = (i,j)
    return bestMove

def printBoard(board):
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    print(" "+ board[0][0] + " "+ "|"+ " "+ board[0][1]+" "+"|"+" "+" "+board[0][2]+" ")
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    print("-------------")
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    print(" "+ board[1][0] + " "+ "|"+ " "+ board[1][1]+" "+"|"+" "+" "+board[1][2]+" ")
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    print("-------------")
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    print(" "+ board[2][0]+ " "+ "|"+ " "+ board[2][1]+" "+"|"+" "+" "+board[2][2]+" ")
    print(" "+ " " + " "+ "|"+ " "+ " "+" "+"|"+" "+" "+" "+" ")
    
def hasWon(board):
    for row in range(0,2):
        if(board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if(board[row][0] == player):
                return (True,player)
            elif(board[row][0] == computer):
                return (True,player)
    for col in range(0,2):
        if(board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if(board[0][col] == player): 
                return (True,player)
            elif(board[0][col] == computer):
                return (True,computer)
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if(board[0][0] == player):
            return (True,player)
        elif(board[0][0] == computer):
            return (True,computer)
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if(board[0][2] == player):
            return (True,player)
        elif(board[0][2] == computer):
            return (True,computer)
    return (False,' ')

while(True):
    player = (input("Do you want to play as X or O: ")).capitalize()
    if (player == 'X'):
        computer = 'O'
        break
    elif(player == 'O'):
        computer = 'X'
        break
    else:
        print("You can only enter either X or O symbols. Please re select your symbol.")

board = [[' ' for i in range(3)] for j in range(3)]
while(isMoveLeft(board) and not hasWon(board)[0]):
    printBoard(board)
    row = int(input("Enter the row of your move (0 to 2 inclusive): "))
    column = int(input("Enter the column of your move (0 to 2 inclusive): "))
    if(row > 2 or row < 0 or column > 2 or column < 0):
        print("Invalid location on board. Please re-enter.")
        continue
    board[row][column] = player
    computerMove = findBestMove(board)
    board[computerMove[0]][computerMove[1]] = computer
    
    
printBoard(board) 
if(hasWon(board)[1] == player):
    print("Congratulations you have won the game.")
else:
    print("Sorry but you lost")    
