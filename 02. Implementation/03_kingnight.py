p = input()

cnt = 0
py = int(ord(p[0]) - 96)
px = int(p[1])

nx = px
ny = py

night_x = [2, 1, 2, 1, -1, -1, -2, -2]
night_y = [1, 2, -1, -2, 2, -2, -1, 1]

for i in range(len(night_x)) :
    nx += night_x[i]
    ny += night_y[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        nx = px
        ny = py
        continue
    else :
        nx = px
        ny = py
        cnt +=1

print(cnt)

# # example
#
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0]))-int(ord('a'))+1
#
# steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
#
# result = 0
#
# for step in steps :
#     next_row = row + step[0]
#     next_col = column + step[1]
#
#     if next_row <= 8 and next_row >= 1 and next_col <= 8 and next_row >= 1 :
#         result += 1
#
# print(result)