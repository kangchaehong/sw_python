from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)

d = [-1] * (n+1)

d[x] = 0
q = deque([x])
while q :
    x = q.popleft()
    for i in graph[x] :
        if d[i] == -1 :
            d[i] = d[x]+1
            q.append(i)

for i in range(1,n+1) :
    if d[i] == k :
        print(i)
if k not in d :
    print(-1)