
class element:
    def __init__(self, x, y, sign, actualX = None, actualY = None):
        self.desiredX = x
        self.desiredY = y
        self.sign = sign

def is_element_correct(el, x, y):
    if x == el.desiredX and y == el.desiredY:
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
