from readFile import readFile
import numpy as np

def splitInput(input_lines):
    numbers = [int(item) for item in input_lines[0].split(',')]
    boards = []
    board = ""
    ii = 0
    for line in input_lines[2:]:
        #print(board)
        if ii < 4:
            board += line+';'
            ii += 1
        elif ii < 5:
            board += line
            ii += 1
            #print(board)
            boards.append(np.matrix(board))
        else:
            board = ""
            ii = 0
    #print(boards)
    return numbers, boards

def findWinner(numbers, boards):
    for number in numbers:
        for board in boards:
            for row in range(0, 5):
                for col in range(0, 5):
                    if board[row, col] == number:
                        board[row, col] = -1
                    if np.all(board[:, col] == -1):
                        return number, board
                if np.all(board[row] == -1):
                    return number, board
        #print(str(number) + ": " + str(boards))

def part1(input_lines):
    #print(input_lines)
    numbers, boards = splitInput(input_lines)
    number, winner = findWinner(numbers, boards)
    print(np.extract(winner != -1, winner).sum()*number)

def removeArray(L, arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind], arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        raise ValueError('array not found in list.')

def findLooser(numbers, boards):
    for number in numbers:
        for board in boards:
            for row in range(0, 5):
                for col in range(0, 5):
                    if board[row, col] == number:
                        board[row, col] = -1
                    if np.all(board[:, col] == -1):
                        if len(boards) == 1:
                            return number, board
                        removeArray(boards, board)
                        return findLooser(numbers[numbers.index(number):], boards)
                if np.all(board[row] == -1):
                    if len(boards) == 1:
                        return number, board
                    removeArray(boards, board)
                    return findLooser(numbers[numbers.index(number):], boards)
        #print(str(number) + ": " + str(boards))

def part2(input_lines):
    #print(input_lines)
    numbers, boards = splitInput(input_lines)
    number, looser = findLooser(numbers, boards)
    print(np.extract(looser != -1, looser).sum()*number)

if __name__ == '__main__':
    inputLines = readFile("input.txt")
    #part1(inputLines)
    part2(inputLines)
