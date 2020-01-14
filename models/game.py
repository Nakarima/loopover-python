class element:
    def __init__(self, x, y, sign):
        self.actualX = x
        self.actualY = y
        self.desiredX = x
        self.desiredY = y
        self.sign = sign
    def isCorrect(self):
        if self.actualX == self.desiredX and self.actualY == self.desiredY:
            return True
        return False

class game:
    def __init__(self, game_id, size):
        self.game_id = game_id
        self.size = size
        self.board = generate_board(size)

    def isSolved(self):
        for row in self.board:
            for element in row:
                if !element.isCorrect:
                    return false
        return true

    def move_up(self, x):
        tmp = self.board[0][x]
        tmp.actualY = size - 1
        for i in range(1, self.size):
            self.board[i][x].actualY -= 1
            self.board[i - 1][x] = self.board[i][x]

        self.board[self.size - 1][x] = tmp

    def move_down(self, x):
        tmp = self.board[self.size - 1][x]
        tmp.actualY = 0
        for i in reversed(range(self.size - 1)):
            self.board[i][x].actualY += 1
            self.board[i + 1][x] = self.board[i][x]

        self.board[0][x] = tmp

    def move_right(self, y):
        tmp = self.board[y][self.size - 1]
        tmp.actualX = 0
        for i in reversed(range(self.size - 1)):
            self.board[y][i].actualX += 1
            self.board[y][i + 1] = self.board[y][i]

        self.board[y][0] = tmp

    def move_left(self, y):
        tmp = self.board[y][0]
        tmp.actualX = self.size - 1
        for i in range(1, self.size):
            self.board[y][i].actualX -= 1
            self.board[y][i - 1] = self.board[y][i]

        self.board[y][self.size - 1] = tmp


def generate_board(size):
    board = []
    sign = 0
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(element(j, i, sign))
            sign += 1

    return board
