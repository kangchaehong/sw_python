from collections import deque
n,m,k,x = map(int, input().split())
city = [[] for _ in range(n+1)]
# for _ in range(m) :
#     city.append(list(map(int, input().split())))
for _ in range(m) :
    a,b = map(int, input().split())
    city[a].append(b)

dist = [-1]*(n+1)
dist[x] = 0
q = deque()
q.append(x)
cnt = 0

while q :
    n = q.popleft()
    for nextnode in city[n] :
        if dist[nextnode] == -1 :
            dist[nextnode] = dist[n] +1
            q.append(nextnode)
    # cnt += 1
    # for i, j in city :
    #     if i == n :
    #         dist[j] = min(dist[j], cnt)
    #         q.append(j)

check = False
for i in range(len(dist)) :
    if dist[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)

