from functools import reduce
from models.element import *

class game_state:
    def __init__(self, game_id, size, board = None, moves_count = None):
        self.game_id = game_id
        self.size = size
        self.board = create_scrambled_board(size) if board is None else board
        self.moves_count = 0 if moves_count is None else moves_count

def is_game_solved(state):
    for i, row in enumerate(state.board):
        for j, el in enumerate(row):
            if not is_element_correct(el, j, i):
               return False
    return True

def move_up(state, x):
    updated_board = state.board
    tmp = updated_board[0][x]
    lastElement = element(tmp.desiredX, tmp.desiredY, tmp.sign)
    for i in range(1, state.size):
        updated_board[i - 1][x] = updated_board[i][x]

    updated_board[state.size - 1][x] = lastElement
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_down(state, x):
    updated_board = state.board
    tmp = updated_board[state.size - 1][x]
    firstElement = element(tmp.desiredX, tmp.desiredY, tmp.sign)
    for i in reversed(range(state.size - 1)):
        updated_board[i + 1][x] = updated_board[i][x]

    updated_board[0][x] = firstElement
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_right(state, y):
    tmp = state.board[y]
    moved_row = [tmp[state.size - 1]] + tmp[:state.size - 1]
    updated_board = state.board
    updated_board[y] = moved_row
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_left(state, y):
    tmp = state.board[y]
    moved_row = tmp[1:] + [tmp[0]]
    updated_board = state.board
    updated_board[y] = moved_row
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def generate_board(size):
    board = []
    sign = 0
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(element(j, i, sign))
            sign += 1

    return board

def create_scrambled_board(size):
    return shuffle(generate_board(size), size)

import random

def shuffle(board, size, rand=random):
    moves = [move_up, move_left, move_down, move_right]
    tmp_state = game_state(-1, size, board)
    for i in range(80):
        tmp_state = moves[random.randint(0, 3)](tmp_state, random.randint(0, size - 1))

    return tmp_state.board
