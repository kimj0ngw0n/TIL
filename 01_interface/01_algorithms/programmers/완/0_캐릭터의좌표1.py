# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    row_lim, col_lim = int((board[0] - 1) / 2), int((board[1] - 1) / 2)

    answer = [0, 0]
    for key in keyinput:
        if key == 'left':
            answer[0] -= 1
            if abs(answer[0]) > row_lim:
                answer[0] += 1
        elif key == 'right':
            answer[0] += 1
            if abs(answer[0]) > row_lim:
                answer[0] -= 1
        elif key == 'up':
            answer[1] += 1
            if abs(answer[1]) > col_lim:
                answer[1] -= 1
        else:
            answer[1] -= 1
            if abs(answer[1]) > col_lim:
                answer[1] += 1
    return answer
