# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

# ["119", "97674223", "1195524421"]	false
# ["97674223", "119", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false

# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.


def solution(phone_book):
    phone_dict = dict()
    min_len = 20

    for key in phone_book:
        phone_dict[key] = key
        if len(key) < min_len:
            min_len = len(key)

    print(phone_dict)

    # 문자열을 잘라서 dict에 일치하는 문자열이 있는지 확인
    # 시간 복잡도 계산 : O(n) * O(n) * O(1) = O(n^2)
    for key in phone_book:  # O(n)
        # for i in range(len(key)):  # O(n) -> 이해하기 쉬운 코드
        for i in range(min_len, len(key)):  # O(n)
            head = key[:i]  # 1 11 119 11194
            print(key, head)
            if phone_dict.get(head) is not None:  # O(1)
                return False

    return True


result = solution(["12","1235","123","1235","567","88"])
print(result)
