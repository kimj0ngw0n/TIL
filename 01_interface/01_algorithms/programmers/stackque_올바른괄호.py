# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false


def solution(s):
    flag = 0
    for parenthesis in s:
        if parenthesis == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False

    if flag > 0:
        return False

    return True


# 스택 풀이
# def solution(s):
#     parenthesis_list = []
#     for parenthesis in s:
#         if parenthesis == '(':
#             parenthesis_list.append(parenthesis)
#         else:
#             if len(parenthesis_list) == 0:
#                 return False
#             if parenthesis_list[-1] == '(':
#                 parenthesis_list.pop()
#
#     if len(parenthesis_list) > 0:
#         return False
#
#     return True


s1 = "()()"
result = solution(s1)
print(result)
