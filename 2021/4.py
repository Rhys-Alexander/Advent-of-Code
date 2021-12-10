from inpt import day4


def getFinalScore(selected_board):
    board, called = selected_board
    board_numbers = [item for row in board for item in row]
    uncalled = sum([num for num in board_numbers if num not in called])
    final_score = called[-1] * uncalled
    return final_score


# Part 1
def checkBoardsForWin(inpt):
    boards, numbers = inpt
    called = []
    for number in numbers:
        called.append(number)
        for board in boards:
            for row in board:
                if all(num in called for num in row):
                    return board, called
            for i in range(len(board[0])):
                col = []
                for row in board:
                    col.append(row[i])
                if all(num in called for num in col):
                    return board, called


print(getFinalScore(checkBoardsForWin(day4())))


# Part 2
def checkBoardsForLoss(inpt):
    boards, numbers = inpt
    called = []

    for number in numbers:
        called.append(number)

        new_boards = []
        for board in boards:
            win = False

            if len(boards) == 1:
                return board, called
            for row in board:
                if all(num in called for num in row):
                    win = True
            for i in range(len(board[0])):
                col = []
                for row in board:
                    col.append(row[i])
                if all(num in called for num in col):
                    win = True

            if not win:
                new_boards.append(board)

        boards = new_boards


print(getFinalScore(checkBoardsForLoss(day4())))
