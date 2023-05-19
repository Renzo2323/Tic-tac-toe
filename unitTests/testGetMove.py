import unittest
import re


class TestGetMove(unittest.TestCase):

    def testGetMoveValid(self): # valid: right format("int,int"), three characters, numbers between 0 and 2
        for x in range(3):  
            for y in range(3):
                self.assertEqual(getMoveTest(str(x) + "," +str(y)), (x,y), "Expected " + str((x, y)))
    
    def testGetMoveInvalid(self): # invalid: wrong fromat, not three characters, numbers not between 0 and 2

        self.assertIsNone(getMoveTest("2,3"), "Expected None")

        for x in range(3, 20):  # over the desired range
            for y in range(4, 20):
                self.assertIsNone(getMoveTest(str(x) + "," +str(y)), "Expected None")

        for x in range(-20, 0):  # under the desired range
            for y in range(-20, 0):
                self.assertIsNone(getMoveTest(str(x) + "," +str(y)), "Expected None")

        for x in range(3):  # wrong format
            for y in range(3):
                self.assertIsNone(getMoveTest(str(x) + " " +str(y)), "Expected None")  # missing a comma
                self.assertIsNone(getMoveTest(str(x) + ",," +str(y)), "Expected None")  # two commas
                self.assertIsNone(getMoveTest(str(x) +str(y)), "Expected None")  # only the two numbers
                self.assertIsNone(getMoveTest(str(x) + ", " +str(y)), "Expected None")  # space after comma



# Takes move argument instead of user input for testing reasons, returns None if move is invalid
def getMoveTest(move):
        if re.match(r'\d,\d', move) and len(move) <= 3:
            splitCoordinates = move.split(',')
            x = int(splitCoordinates[0])
            y = int(splitCoordinates[1])

            if int(x) in range(0, 3) and int(y) in range(0, 3):
                return (x, y)
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    unittest.main()