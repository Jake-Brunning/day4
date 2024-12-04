possibleMoves = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1, 1)]


#read every line in the file
def readFile(filepath: str) -> list[str]:
    file = open(filepath, 'r')
    return file.readlines()


#count the amount of correct searches
def correctSearches(targets: str, board : list[str]) -> int:
    HEIGHT = len(board)
    WIDTH = len(board[0])

    total = 0

    for x in range (0, HEIGHT):
        for y in range (0, WIDTH):
            total += checkX(board, (x,y), targets)

    return total


#inputs a target and outputs the amount of words you can form at that place
def goThroughPossibleMoves(board: list[str], pos: tuple[int, int], target: str) -> int:
    total = 0

    for move in possibleMoves:
        total += getValidWords(board, pos, target)

    return total

def checkX(board: list[str], pos: tuple[int, int], target: str) -> int:
   #x going rightwords from the current word. second part is checking going up from the word 2 below
    xGoingRight = getValidWords(pos, (1, 1), target, board) + getValidWords((pos[0] + 2, pos[1]), (-1, 1), target, board)
    xGoingRightReversed = getValidWords(pos, (1, 1), target[::-1], board) +  getValidWords((pos[0] + 2, pos[1]), (-1, 1), target[::-1], board)

    if xGoingRight + xGoingRightReversed == 2:
       return 1

    return 0

#checks if a word moving along the specified axis is valid
def getValidWords(pos: tuple[int, int], moving: tuple[int, int], target: str, input: list[str]) -> int:
    letterLookingAt = getLetterLookingAt(input, pos) #get the letter being looked at in the string

    #check if the letter is in the row or diagonal etc
    for x in target:
        if letterLookingAt != x:
            return 0
        else:
            pos = addTuple(pos, moving)
            letterLookingAt = getLetterLookingAt(input, pos)
    
    return 1
    
def getLetterLookingAt(board: list[str], pos: tuple[int, int]) -> str:
    #if we are out of bounds
    test = board[0]
    test2 = len(test)
    if pos[0] >= len(board) or pos[1] > len(board[0]) - 2 or pos[0] < 0 or pos[1] < 0:
        return "*" #error char
    
    return board[pos[0]][pos[1]]

#adds two tuples
def addTuple(tuple1: tuple[int, int], tuple2: tuple[int, int]) -> tuple[int, int]:
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


if __name__ == '__main__':
    print(correctSearches("MAS", readFile("input.txt")))