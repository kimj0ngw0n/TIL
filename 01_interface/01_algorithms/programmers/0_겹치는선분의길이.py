# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def get_and_line(a, b):
    if a[0] > b[0]:
        if b[1] - a[0] > 0:
            if b[1] - a[1] > 0:
                return [a[0], a[1]]
            else:
                return [a[0], b[1]]
        else:
            return [0, 0]
    elif a[1] > b[0]:
        if b[1] < a[1]:
            return [b[0], b[1]]
        else:
            return [b[0], a[1]]
    else:
        return [0, 0]


def get_len(line):
    return line[1] - line[0]


def solution(lines):

    l1 = lines[0]
    l2 = lines[1]
    l3 = lines[2]

    l1al2 = get_and_line(l1, l2)
    l2al3 = get_and_line(l2, l3)
    l3al1 = get_and_line(l3, l1)

    l1al2al3 = get_and_line(l1al2, l3)

    answer = get_len(l1al2) + get_len(l2al3) + get_len(l3al1) - 2 * get_len(l1al2al3)

    return answer
