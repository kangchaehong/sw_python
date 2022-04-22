from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)
result = [-1]*(n+1)
result[x] = 0

def bfs() :
    q = deque([x])

    while q :
        start = q.popleft()
        for next_node in graph[start] :
            if result[next_node] == -1 :
                result[next_node] = result[start] +1
                q.append(next_node)

    check = False
    for i in range(len(result)) :
        if result[i] == k :
            print(i)
            check = True
    if check == False :
        print(-1)
bfs()