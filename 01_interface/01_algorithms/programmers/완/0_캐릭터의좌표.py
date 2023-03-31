# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def goleft(coor):
    return [coor[0] - 1, coor[1]]


def goright(coor):
    return [coor[0] + 1, coor[1]]


def goup(coor):
    return [coor[0], coor[1] + 1]


def godown(coor):
    return [coor[0], coor[1] - 1]


def move(pieces, direction):
    if direction == 'left':
        return goleft(pieces)
    elif direction == 'right':
        return goright(pieces)
    elif direction == 'up':
        return goup(pieces)
    elif direction == 'down':
        return godown(pieces)
    else:
        print('move error!')


def solution(keyinputs, board):
    coor = [0, 0]
    cantmove = int((board[0] - 1) / 2), int((board[1] - 1) / 2)

    for keyinput in keyinputs:
        if not (
                (coor[0] == cantmove[0] and keyinput == 'right') or
                (coor[0] == -cantmove[0] and keyinput == 'left') or
                (coor[1] == cantmove[1] and keyinput == 'up') or
                (coor[1] == -cantmove[1] and keyinput == 'down')
        ):
            coor = move(coor, keyinput)

        # print(keyinput, coor)

    return coor
