def get_idx(id_list, id):
    return id_list.index(id)

def solution(id_list, reports, k):

    # rdb 생성
    rdb = [[0 for _ in id_list] for _ in id_list]
    for report in reports:
        reporter, reported = report.split()
        reporter = get_idx(id_list, reporter)
        reported = get_idx(id_list, reported)
        rdb[reporter][reported] = 1

    # banlist 생성
    banlist = [0 for _ in id_list]
    for col in range(len(id_list)):
        total = 0
        for row in range(len(id_list)):
            total += rdb[row][col]
        if total >= k:
            banlist[col] = 1

    answer = []
    for row in rdb:
        total = 0
        for idx, col in enumerate(row):
            if banlist[idx] and col:
                total += 1
        answer.append(total)

    return answer