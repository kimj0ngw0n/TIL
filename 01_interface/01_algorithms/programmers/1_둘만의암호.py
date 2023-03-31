# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def get_real_alpha(skip):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for remove_alpha in skip:
        alpha = alpha.replace(remove_alpha, '')

    return alpha


def alpha_plus_index(letter, real_alpha, index):
    plus_index = real_alpha.index(letter) + index

    return real_alpha[plus_index % len(real_alpha)]


    '''
    if plus_index >= len(real_alpha):
        return real_alpha[plus_index - len(real_alpha)]
    else:
        return real_alpha[plus_index]
    '''


def solution(s, skip, index):
    answer = ''
    real_alpha = get_real_alpha(skip)

    for letter in s:
        answer += alpha_plus_index(letter, real_alpha, index)

    return answer


# "happy"
print(solution("aukks", "wbqd", 5))
