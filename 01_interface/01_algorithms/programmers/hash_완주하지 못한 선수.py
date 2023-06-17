# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# participant	            completion	            return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

# pDict 설계
# key(이름) : value(개수)


def solution(participant, completion):
    pNameToNumberDict = dict()

    # Dictionary에 넣는 작업
    for name in participant:
        if pNameToNumberDict.get(name) is None:
            pNameToNumberDict[name] = 0
        pNameToNumberDict[name] += 1

    # print(pNameToNumberDict)


    # Dictionary에서 빼는 작업
    for name in completion:
        pNameToNumberDict[name] -= 1
        if pNameToNumberDict[name] == 0:
            pNameToNumberDict.pop(name)

    # print(pNameToNumberDict)

    return pNameToNumberDict.popitem()[0]


# participant1 = ["mislav", "stanko", "mislav", "ana"]
# completion1 = ["stanko", "ana", "mislav"]
#
# result = solution(participant1, completion1)
# print(result)
