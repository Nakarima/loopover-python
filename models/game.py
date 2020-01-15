class element:
    def __init__(self, x, y, sign, actualX = None, actualY = None):
        self.actualX = actualX if actualX is not None else x
        self.actualY = actualY if actualY is not None else y
        self.desiredX = x
        self.desiredY = y
        self.sign = sign
    def isCorrect(self):
        if self.actualX == self.desiredX and self.actualY == self.desiredY:
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

class game:
    def __init__(self, game_id, size):
        self.game_id = game_id
        self.size = size
        self.board = generate_board(size)
        self.movesCount = 0

    def isSolved(self):
        for row in self.board:
            for element in row:
                if not element.isCorrect:
                    return false
        return true

    def move_up1(self, x): pass
       # self.movesCount, self.board = move_up(self.board, x, self.movesCount, self.size)
        #self.movesCount += 1
        #tmp = self.board[0][x]
        #tmp.actualY = size - 1
        #for i in range(1, self.size):
        #    self.board[i][x].actualY -= 1
        #    self.board[i - 1][x] = self.board[i][x]

        #self.board[self.size - 1][x] = tmp

    def move_down(self, x):
        self.movesCount += 1
        tmp = self.board[self.size - 1][x]
        tmp.actualY = 0
        for i in reversed(range(self.size - 1)):
            self.board[i][x].actualY += 1
            self.board[i + 1][x] = self.board[i][x]

        self.board[0][x] = tmp

    def move_right(self, y):
        self.movesCount += 1
        tmp = self.board[y][self.size - 1]
        tmp.actualX = 0
        for i in reversed(range(self.size - 1)):
            self.board[y][i].actualX += 1
            self.board[y][i + 1] = self.board[y][i]

        self.board[y][0] = tmp

    def move_left(self, y):
        self.movesCount += 1
        tmp = self.board[y][0]
        tmp.actualX = self.size - 1
        for i in range(1, self.size):
            self.board[y][i].actualX -= 1
            self.board[y][i - 1] = self.board[y][i]

        self.board[y][self.size - 1] = tmp

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

def generate_board(size):
    board = []
    sign = 0
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(element(j, i, sign))
            sign += 1

    return board
