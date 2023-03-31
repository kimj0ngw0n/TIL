# https://school.programmers.co.kr/learn/courses/30/lessons/160586

max_key_map = 101


def solution(keymap, targets):

    answer = []
    keymaps = [['' for _ in range(max_key_map)] for _ in range(max_key_map)]

    for i, keys in enumerate(keymap):
        for j, key in enumerate(keys):
            keymaps[i][j] = key

    for target in targets:
        total = 0

        for tar in target:

            for i in range(max_key_map):
                is_line_empty = -1

                for j in range(max_key_map):
                    if keymaps[j][i] == tar:
                        is_line_empty = 0
                        break
                    elif keymaps[j][i]:
                        is_line_empty = 1

                total += 1

                if is_line_empty == 0:
                    break
                elif is_line_empty == -1:
                    total = -1
                    break

            if total == -1:
                break

        answer.append(total)

    return answer
