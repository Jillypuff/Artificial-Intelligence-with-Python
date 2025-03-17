"""
Tic Tac Toe Player
"""

import math

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
    return X if sum(row.count(EMPTY) for row in board) % 2 == 1 else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell != EMPTY for cell in row) for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None, utility(board)

    player_turn = player(board)
    best_action = None
    if player_turn == X:
        best_action, _ = max_value(board)
    else:
        best_action, _ = min_value(board)
    return best_action

def max_value(board):
    if terminal(board):
        return None, utility(board)
    v = -math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        _, new_v = min_value(new_board)
        if new_v > v:
            v = new_v
            best_action = action
    return best_action, v


def min_value(board):
    if terminal(board):
        return None, utility(board)
    v = math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        _, new_v = max_value(new_board)
        if new_v < v:
            v = new_v
            best_action = action
    return best_action, v