# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3

# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

# 1. 장르별 재생 시간으로 정렬하여 map-list로 구현
#  classic - 800:3, 500:0, 150:2
#  pop     - 2500:4, 600:1
# 2. 전체 재생시간을 구하고 장르별 베스트앨범 우선순위를 정리
#  1순위 : pop - 2500:4, 600:1
#  2순위 : classic - 800:3, 500:0, 150:2
# 3. 시간으로 정렬된 장르에서 곡을 2개씩 뽑아서 index로 배열을 만든다.
#  4, 1, 3, 0

def solution(genres, plays):
    answer = []
    genres_allplay_dict = dict()  # 문자열-정수, 장르하고 모든 플레이횟수를 sum을 한 맵
    genres_plays_dict = dict()  # 문자열-list-list, 장르-플레이횟수-index

    ########## 초기화 부 ##########
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # genres_alltime_dict 생성
        genres_allplay_dict[genre] = genres_allplay_dict.get(genre, 0) + int(play)  # dict.get(key, key가 없을 때 default 값 지정)

        # genres_plays_dict 생성
        if genres_plays_dict.get(genre) is None:
            genres_plays_dict[genre] = list()
        genres_plays_dict[genre].append([i, play])

    # print(genres_allplay_dict)
    # print(genres_plays_dict)

    ########## 풀이 부 ##########
    # 장르별 우선순위를 선정
    # sorted('장르-시간의 셋', '정렬 알고리즘 - 시간으로 정렬하는 lambda', '역순 정렬 옵션')
    genres_allplay_sorted_list = sorted(genres_allplay_dict.items(), key=lambda x: x[1], reverse=True)
    # print(genres_allplay_sorted_list)

    # 선정된 장르별로 순회하면서 2곡 뽑아오기
    for genre, play in genres_allplay_sorted_list:
        # print(genres_plays_dict[genre])
        # 장르별 우선순위 선정을 위한 정렬
        pick_list = sorted(genres_plays_dict[genre], key=lambda x: x[1], reverse=True)[:2]
        # print("pick_list :", pick_list)

        for i, play in pick_list:
            answer.append(i)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = solution(genres, plays)
print(result)
