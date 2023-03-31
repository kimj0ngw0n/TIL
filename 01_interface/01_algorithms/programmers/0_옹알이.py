def solution(babbling):
    answer = 0
    baby = 'aya', 'ye', 'woo', 'ma'

    for babble in babbling:
        say = ''
        for bab in babble:
            say += bab
            if say in baby:
                say = ''
        if say == '':
            answer += 1

    return answer
