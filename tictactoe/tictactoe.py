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
    ans = 0
    for i in board:
        for j in i:
            if j!=EMPTY:
                ans +=1

    if ans%2 == 0:
        return X
    else:
        return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                ans = ans + [(i,j)]

    return ans
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newboard = copy.deepcopy(board)
    if board[action[0]][action[1]] != None:
        raise ValueError
    turn = player(board)
    newboard[action[0]][action[1]] = turn
    return newboard
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        win = True
        if board[i][0] == EMPTY:
            continue
        for j in range(1,3):
            if board[i][j]!=board[i][0]:
                win = False
                break
        if win :
            return board[i][0]

    for i in range(3):
        win = True
        if board[0][i] == EMPTY:
            continue
        for j in range(1,3):
            if board[j][i]!=board[0][i]:
                win = False
                break
        if win :
            return board[0][i]

    if board[0][0] != EMPTY:
        win = True
        for i in range(1,3):
            if board[i][i] != board[0][0]:
                win = False
                break
        if win :
            return board[0][0]
    if board[0][2] != EMPTY:
        win = True
        for i in range(1,3):
            if board[i][2-i] != board[0][2]:
                win = False
                break
        if win :
            return board[0][2]
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in board:
            for j in i:
                if j == EMPTY:
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    W = winner(board)
    if W == X:
        return 1
    elif W == O:
        return -1
    else:
        return 0
    raise NotImplementedError

def bestutility(board):
    if terminal(board):
        return utility(board)
    action = actions(board)
    turn = player(board)
    if turn == X:
        max = -5
        for i in action:
            v = bestutility(result(board,i))
            if v > max:
                max = v
        return max
    else:
        max = 5
        for i in action:
            v = bestutility(result(board,i))
            if v < max:
                max = v
        return max
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    action = actions(board)
    ans = ()
    turn = player(board)

    if turn == X:
        max = -5
        for i in action:
            v = bestutility(result(board,i))
            if v > max:
                max = v
                ans = i
    else:
        max = 5
        for i in action:
            v = bestutility(result(board,i))
            if v < max:
                max = v
                ans = i
    return ans
