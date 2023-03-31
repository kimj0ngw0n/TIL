def solution(wallpaper):

    start_row = start_col = 51
    end_row = end_col = 0

    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                if row < start_row:
                    start_row = row
                if col < start_col:
                    start_col = col
                if row+1 > end_row:
                    end_row = row+1
                if col+1 > end_col:
                    end_col = col+1

    answer = [start_row, start_col, end_row, end_col]

    return answer
