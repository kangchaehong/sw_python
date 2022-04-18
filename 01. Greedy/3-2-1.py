n, m, k = map(int, input().split())
sumlist = list(map(int, input().split()))
# sumlist.sort(reverse=True)
# sum = 0
#
# for i in range(m) :
#     if i % k == 0 and i != 0:
#         sum += sumlist[1]
#     else :
#         sum += sumlist[0]
#
# print(sum)
#

sumlist.sort()
first = sumlist[-1]
second = sumlist[-2]

# 큰수를 더하는 개수 구하기
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
