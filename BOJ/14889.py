# # 입력부
# n = int(input())
# team = []
# start = 0
# link = 0
# for i in range(n) :
#     team.append(list(map(int, input().split())))
# fcomb = []
# for i in range(n) :
#     fcomb.append(i)
# diff = 1e9
#
# def comb(arr, n) :
#     result = []
#     if len(arr) < n :
#         return arr
#     if n == 1 :
#         for i in arr :
#             result.append([i])
#     if n > 1 :
#         for i in range(int(len(arr)-n+1)) :
#             for j in comb(arr[i+1:], n-1) :
#                 result.append([arr[i]]+j)
#     return result
#
# result = comb(fcomb, len(fcomb)/2)
# for res in result :
#     # print(res)
#     r2 = list(set(fcomb)-set(res))
#     for r in comb(res,2) :
#         # print('1',r)
#         start += team[r[0]][r[1]]
#         start += team[r[1]][r[0]]
#     for r in comb(r2,2) :
#         # print('2',r)
#         link += team[r[0]][r[1]]
#         link += team[r[1]][r[0]]
#     # for i in range(n) :
#     #     for j in range(i+1,n) :
#     #         if i in res and j in res:
#     #             # print('s',i,j)
#     #             start += team[i][j]
#     #             start += team[j][i]
#     #         if i not in res and j not in res:
#     #             # print(';', i, j)
#     #             link += team[i][j]
#     #             link += team[j][i]
#     diff = min(diff, abs(start-link))
#     start = 0
#     link = 0
# print(diff)
from itertools import permutations, combinations
from collections import deque

n = int(input())
k = [list(map(int, input().split()))
for _ in range(n)]
t = [i for i in range(n)]
INF = 10000
ans = INF
q = deque(combinations(t, n//2))
print(q)
start_team = deque()
link_team = deque()
for _ in range(len(q)//2):
    start_team.append(q.popleft())
    link_team.append(q.pop())
def calcStat(team):
    ln = len(team)
    s = 0
    for x in range(0, ln-1):
        for y in range(x+1, ln):
            s += k[team[x]][team[y]] + k[team[y]][team[x]]
    return s
for i in range(len(start_team)):
    ans = min(ans, abs(calcStat(start_team[i]) - calcStat(link_team[i])))
print(ans)