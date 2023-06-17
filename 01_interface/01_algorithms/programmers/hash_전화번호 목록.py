# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

# ["119", "97674223", "1195524421"]	false
# ["97674223", "119", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false

# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

def solution(phone_book):
    min_len = 20
    phone_dict = dict()

    for key in phone_book:
        if len(key) < min_len:
            min_len = len(key)
        phone_dict[key] = key

    # print(phone_dict)

    for key in phone_book:
        for i in range(min_len, len(key)):
            if phone_dict.get(key[:i]) is not None:
                return False

    return True


result = solution(["12","123","1235","567","88"])
print(result)
