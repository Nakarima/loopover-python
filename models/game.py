class element:
    def __init__(self, x, y, sign, actualX = None, actualY = None):
        self.actualX = actualX if actualX is not None else x
        self.actualY = actualY if actualY is not None else y
        self.desiredX = x
        self.desiredY = y
        self.sign = sign

def is_element_correct(el):
    if el.actualX == el.desiredX and el.actualY == el.desiredY:
        return True
    return False

def move_up_element(el):
    return element(el.desiredX, el.desiredY, el.sign, el.actualX, el.actualY - 1)

def move_down_element(el):
    return element(el.desiredX, el.desiredY, el.sign, el.actualX, el.actualY + 1)

def move_right_element(el):
    return element(el.desiredX, el.desiredY, el.sign, el.actualX + 1, el.actualY)

def move_left_element(el):
    return element(el.desiredX, el.desiredY, el.sign, el.actualX - 1, el.actualY)


class game_state:
    def __init__(self, game_id, size, board = None, moves_count = None):
        self.game_id = game_id
        self.size = size
        self.board = generate_board(size) if board is None else board
        self.moves_count = 0 if moves_count is None else moves_count

def is_game_solved(state):
    for row in state.board:
        for el in row:
            if not is_correct(el):
                return false
    return true

def move_up(state, x):
    updated_board = [list(
        map(lambda el: move_up_element(el) if el.actualX == x else el, row)
    ) for row in state.board]
    tmp = updated_board[0][x]
    lastElement = element(tmp.desiredX, tmp.desiredY, tmp.sign, tmp.actualX, state.size - 1)
    #no idea here for immutable
    for i in range(1, state.size):
        updated_board[i - 1][x] = updated_board[i][x]

    updated_board[state.size - 1][x] = lastElement
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_down(state, x):
    updated_board = [list(
        map(lambda el: move_down_element(el) if el.actualX == x else el, row)
    ) for row in state.board]
    tmp = updated_board[state.size - 1][x]
    firstElement = element(tmp.desiredX, tmp.desiredY, tmp.sign, tmp.actualX, 0)
    #no idea here for immutable
    for i in reversed(range(state.size - 1)):
        updated_board[i + 1][x] = updated_board[i][x]

    updated_board[0][x] = firstElement
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_right(state, y):
    updated_row = list(map(lambda el: move_right_element(el), state.board[y]))
    moved_row = [updated_row[state.size - 1]] + updated_row[:state.size - 1]
    updated_board = state.board
    updated_board[y] = moved_row
    return game_state(state.game_id, state.size, updated_board, state.moves_count + 1)

def move_left(state, y):
    updated_row = list(map(lambda el: move_left_element(el), state.board[y]))
    moved_row = updated_row[1:] + [updated_row[0]]
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
