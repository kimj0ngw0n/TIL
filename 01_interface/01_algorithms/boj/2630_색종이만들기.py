# https://www.acmicpc.net/problem/2630


# 전역 변수
T = int(input())
colors = []


# 입력
paper = []
for _ in range(T):
    paper.append(list(map(int, input().split())))


# 함수
## 확인 함수
def is_one(pieces):
    piece_color = pieces[0][0]
    for line in pieces:
        for piece in line:
            if piece_color != piece:
                return False
    return True


## 종이 4개로 찢기
def four(pieces):
    half = len(pieces) // 2
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    for i in range(half):
        p1.append(pieces[i][:half])
        p2.append(pieces[i][half:])
        p3.append(pieces[i + half][:half])
        p4.append(pieces[i + half][half:])
    return p1, p2, p3, p4


## 문제 풀이 함수
def div_paper(piece):
    if type(piece) == int:
        return colors.append(piece)
    elif is_one(piece):
        return colors.append(piece[0][0])
    else:
        pieces = four(piece)
        for p in pieces:
            div_paper(p)


## 메인
div_paper(paper)
whites = colors.count(0)
blues = colors.count(1)
print(whites)
print(blues)
