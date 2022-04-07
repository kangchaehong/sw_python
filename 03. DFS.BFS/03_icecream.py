def dfs(x,y) :
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if ice[x][y] == 0 :
        # 갔던곳 방문 처리
        ice[x][y] = 1
        # 상하좌우 재귀적 처리
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
ice = []
count = 0
for i in range(n) :
    ice.append(list(map(int, input())))
# visited = [[0]*n for i in range(m)]

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True :
            result += 1

print(result)

#
# def dfs(ice, v, visited) :
#     visited[v] = True
#
#     for i in ice[v] :
#         if not visited[v] :
#             dfs(ice, i, visited)
#
#     return count
