# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3

# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3

# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

def solution(clothes):
    names = set()
    for cloth in clothes:
        names.add(cloth[1])

    num = dict()
    for cloth in clothes:
        name = cloth[1]
        if name in num.keys():
            num[name] += 1
        else:
            num[name] = 2

    answer = 1
    for key in num.keys():
        answer *= num[key]
    answer -= 1

    return answer
