a = int(input())
b = list(map(int, input().split()))
b.sort()

group = 0
cnt = 1

for i in range(a) :
    if b[i] == cnt :
        cnt = 0
        group += 1
    else :
        cnt += 1
print(group)

# # example
# group = 0
# cnt = 0
#
# for i in b :
#     cnt += 1
#     if cnt >= i :
#         cnt = 0
#         group += 1
# print(group)
