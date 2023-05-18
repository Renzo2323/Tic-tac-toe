import re

def newBoard():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

def newFilledBoard():
    return [['X', 'O', 'O'],
            ['X', 'X', 'X'],
            ['X', 'O', 'O']]


def render(board):

    def noneToEmptySquare(square):
        if square is None:
            return " "
        else:
            return square
    
    print("    0 1 2")
    print("   -------")
    print("0 | " +noneToEmptySquare(board[0][0]) + " " + noneToEmptySquare(board[0][1]) + " " + noneToEmptySquare(board[0][2]) + " |")
    print("1 | " +noneToEmptySquare(board[1][0]) + " " + noneToEmptySquare(board[1][1]) + " " + noneToEmptySquare(board[1][2]) + " |")
    print("2 | " +noneToEmptySquare(board[2][0]) + " " + noneToEmptySquare(board[2][1]) + " " + noneToEmptySquare(board[2][2]) + " |")

    print("   -------")
    
    

def getMove(player):
    print(f"Player {player}, What is your move? (\"0,1\", \"2,2\", \"1,0\", etc)")
    while True:
        coordinates = input()
        if re.match(r'\d,\d', coordinates) and len(coordinates) <= 3:
            splitCoordinates = coordinates.split(',')
            x = splitCoordinates[0]
            y = splitCoordinates[1]

            if int(x) in range(0, 3) and int(y) in range(0, 3):
                return (x, y)
            else:
                print("Only 0, 1 and 2 are valid")
        else:
            print("Must be in this format: x,y")

def makeMove(board, move, player):
    if not isValidMove(board, move):
        raise Exception("Square already taken")
    board[int(move[0])][int(move[1])] = player
    return board

def isValidMove(board, move):
    if board[int(move[0])][int(move[1])] is None:
        return True
    else:
        return False

def getWinner(board):
    h1 = [board[0][0], board[0][1], board[0][2]]
    h2 = [board[1][0], board[1][1], board[1][2]]
    h3 = [board[2][0], board[2][1], board[2][2]]

    v1 = [board[0][0], board[1][0], board[2][0]]
    v2 = [board[0][1], board[1][1], board[2][1]]
    v3 = [board[0][2], board[1][2], board[2][2]]

    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[2][0], board[1][1], board[0][2]]
    lines = [h1, h2, h3, v1, v2, v3, d1, d2]
    for l in lines:
        if l[0] == l[1] == l[2] != None:
            return l[0]
    return None

def isBoardFull(board):
    if None not in board[0] and None not in board[1] and None not in board[2]:
        return True
    else:
        return False


board = newBoard()


render(board)

player = 'X'
while True:


    while True:
        try:
            move = getMove(player)
            board = makeMove(board, move, player)
            break
        except Exception as e:
            print(e)

    render(board)

    winner = getWinner(board)
    if winner is not None:
        print("Hurray!", winner, "wins!")
        break

    if isBoardFull(board):
        print("Draw")
        break


    if(player == 'X'):
        player = 'O'
    else:
        player = 'X'

