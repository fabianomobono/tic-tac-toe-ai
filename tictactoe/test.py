import copy
X = "X"
O = "O"
EMPTY = None

board = [[X, EMPTY, O],[EMPTY, O, EMPTY],[EMPTY,EMPTY,X]]
def player(board):


    """
    Returns player who has the next turn on a board.
    """

    # count number of X and O
    number_of_X = 0
    number_of_O = 0

    # count X's
    for l in board:
       f = l.count(X)
       number_of_X += f

    # count O's
    for li in board:
        g = li.count(O)
        number_of_O += g

    # if there are more X then O
    if number_of_X > number_of_O:
        return O

    else:
        return X

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res = copy.deepcopy(board)
    p = player(board)

    if res[action[0]][action[1]] == EMPTY:
        res[action[0]][action[1]] = p
    else:
        raise NameError("This move is not allowed")

    return res

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for horizontal wins for X
    checker = 0
    checkor = 0
    row = 0
    position = 0
    for l in board:
        for p in l:
            if board[row][position] == X:
                checker += 1
            elif board[row][position] == O:
                checkor += 1
            position += 1
            if checker == 3:
                return X
            if checkor == 3:
                return O
        row += 1
        position = 0
        checker = 0
        checkor = 0

    # check for vertical wins for X
    checker = 0
    checkor = 0
    row = 0
    position = 0
    for i in board[0]:
        for l in board:
            if board[row][position] == X:
                checker += 1

            if board[row][position] == O:
                checkor += 1
            row += 1
            if checker == 3:
                return X

            if checkor == 3:
                return O

        checker = 0
        checkor = 0
        position += 1
        row = 0

    # check for diagonal wins for X
    counter = 0
    checker = 0
    checkor = 0
    for l in board:
        if l[counter] == X:
            checker += 1

        if l[counter] == O:
            checkor += 1


        if checker == 3:
            return X

        if checkor == 3:
            return O
        counter += 1

    counter = 2
    checker = 0
    checkor = 0
    for l in board:
        if l[counter] == X:
            checker += 1
        if l[counter] == O:
            checkor += 1
        if checker == 3:
            return X
        if checkor == 3:
            return O

        counter -= 1
    return 'nope'

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for l in board:
        for p in l:
            if p == EMPTY:
                return False

    return True

print(terminal(board))
