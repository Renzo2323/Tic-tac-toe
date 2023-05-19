import unittest


class TestGetWinner(unittest.TestCase):

    def testGetWinner(self):
        for x in range(2): #Loops twice, once for 'X' and once for 'O'
            if x == 1:
                player = 'X'
            else:
                player = 'O'

            #Horizontal
            winBoard1 =[[player, player, player],
                        [None, None, None],
                        [None, None, None]]
            
            winBoard2 =[[None, None, None],
                        [player, player, player],
                        [None, None, None]]
            
            winBoard3 =[[None, None, None],
                        [None, None, None],
                        [player, player, player]]
            
            #Vertical
            winBoard4 =[[player, None, None],
                        [player, None, None],
                        [player, None, None]]
            
            winBoard5 =[[None, player, None],
                        [None, player, None],
                        [None, player, None]]
            
            winBoard6 =[[None, None, player],
                        [None, None, player],
                        [None, None, player]]
            
            #Diagonal
            winBoard7 =[[player, None, None],
                        [None, player, None],
                        [None, None, player]]
            
            winBoard8 =[[None, None, player],
                        [None, player, None],
                        [player, None, None]]
            
            winBoardList = [winBoard1, winBoard2, winBoard3, winBoard4, winBoard5, winBoard6, winBoard7, winBoard8]

            for winBoard in winBoardList:
                resultWinner = getWinner(winBoard)
                self.assertEqual(resultWinner, player, "Expected " + player)
                
            


        




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


if __name__ == '__main__':
    unittest.main()