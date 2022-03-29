n, m, k = map(int, input().split())
data = list(map(int, input().split()))
#
# sum = 0
# cnt = 0
#
# data.sort()
#
# for i in range(m) :
#     if cnt == k :
#         sum += data[-2]
#         cnt = 0
#     else :
#         sum += data[-1]
#         cnt += 1
#
# print(sum)

# example
data. sort()
sum = 0

first = data[-1]
second = data[-2]

cnt = (m / k+1) * k
cnt += m % (k+1)

sum += cnt * first
sum += (m-cnt) * second

print(sum)


