import unittest


class TestMakeMove(unittest.TestCase):

    def testMakeMoveTakenSquare(self): 
        board = newBoard() #New empty board
        board = makeMove(board, (1,1), 'X')
        expectedBoard =[[None, None, None],
                        [None, 'X', None],
                        [None, None, None]]
        self.assertEquals(board, expectedBoard) #Places X in desired square

        with self.assertRaises(Exception): #Taken square
            makeMove(board, (1,1), 'O')

        


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

def newBoard():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


if __name__ == '__main__':
    unittest.main()