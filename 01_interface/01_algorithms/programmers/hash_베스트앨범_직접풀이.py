# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

# 정의
# {
#   'classic' : 1450,
#   'pop'     : 3100,
# }

# 장르 정렬
# [
#   ['pop'     , [1: 600, 4:2500],],
#   ['classic' , [0: 500, 2:150, 3:800],],
# ]

# 노래 정렬
# [
#   ['pop'     : [[4, 2500], [1, 600]],],
#   ['classic' : [[3, 800], [0, 500], [2, 150]],],
# ]


def solution(genres, plays):
    answer = []
    genres_sum_dict = dict()
    genres_plays_dict = dict()

    # 장르별 플레이 횟수 합계
    for i in range(len(genres)):
        genres_sum_dict[genres[i]] = genres_sum_dict.get(genres[i], 0) + plays[i]

        # 장르별 고유번호, 플레이 횟수
        if genres_plays_dict.get(genres[i]) is None:
            genres_plays_dict[genres[i]] = list()
        genres_plays_dict[genres[i]].append([i, plays[i]])

    # print(genres_sum_dict)
    # print(genres_plays_dict)

    genres_allplay_sorted_list = sorted(genres_sum_dict.items(), key=lambda x: x[1], reverse=True)

    # print(genres_allplay_sorted_list)

    for genre, _ in genres_allplay_sorted_list:
        plays_list = sorted(genres_plays_dict[genre], key=lambda x: x[1], reverse=True)[:2]

        for i, play in plays_list:
            answer.append(i)

    return answer


genres1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]
result = solution(genres1, plays1)
print(result)
