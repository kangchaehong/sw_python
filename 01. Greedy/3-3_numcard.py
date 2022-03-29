row, col = map(int, input().split())
card = []
minv = 0
maxv = 0

for i in range(row) :
    card.append(list(map(int, input().split())))

for i in card :
    minv = min(i)
    if maxv < minv :
        maxv = minv

print(maxv)

# example

# result = 0
# for i in range(row) :
#     data = list(map(int, input().split()))
#     minv = min(data)
#     result = max(minv, result)
#
# print(result)

