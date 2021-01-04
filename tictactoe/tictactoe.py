"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    # for each row
    row = 0
    position = 0
    for l in board:

        # for each position in that row
        for p in l:

            # if that position is empty
            if p == EMPTY:
                actions.add((row, position))

            # go to next position
            position += 1

        # reset position, go to next row
        position = 0
        row += 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # copy the board; what is a deepcopy?
    res = copy.deepcopy(board)

    # figure out who's turn it is
    p = player(board)

    # make sure it's a legal move
    if res[action[0]][action[1]] == EMPTY:

        res[action[0]][action[1]] = p

    # raise an error if it is not
    else:
        raise NameError("This move is not allowed")

    # return what the board would look like if the action would have been taken
    return res

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for horizontal wins
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

    # check for vertical wins
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

    # check for diagonal win
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

    # check for the other diagonal win
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
    return None

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


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    elif winner(board) == O:
        return -1

    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # the board is in a terminal state
    if terminal(board):
        return None

    # if max player
    if player(board) == X:
        v = -1000

        # for every possible action in the board that has been passed to minimax
        for action in actions(board):

            # get the max value between v and min_value(result(board,action))

            max_so_far = max(v, min_value(result(board,action), -9999, 9999))

            # store the highest value out of all the actions
            if max_so_far > v:
                v = max_so_far
                best_move = action

    # if it's the min player's turn
    else:
        v = 1000

        # for every possible action in the board that has been passed to minimax
        for action in actions(board):

            # get the minimum value between v and max(value(result(board, action)))
            min_so_far = min(v, max_value(result(board, action), -9999, 9999))

            # store the highest value out of all the actions
            if min_so_far < v:
                v = min_so_far
                best_move = action
    return best_move


def max_value(board, alpha, beta):
    # if the passed board is in a terminal state
    if terminal(board):
        # return the utility value of this board
        
        return utility(board)
    else:
        v = -1000
        
        for action in actions(board):
            # for every action in the board that has been passed in
            # v = maximum value between v adn min_value(result(board, action)))

            v = max(v, min_value(result(board, action),alpha, beta))
            alpha = max(v,alpha)
            
            if alpha > beta:
                break
        # at the end of the loop return v

        return v

def min_value(board, alpha, beta):
    if terminal(board):

        return utility(board)

    else:
        v = 1000
        
        for action in actions(board):

            v = min(v, max_value(result(board, action), alpha, beta))
            
            beta = min(v, beta)
            if alpha > beta:
                break

        return v
