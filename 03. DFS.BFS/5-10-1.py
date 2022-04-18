n, m = map(int, input().split())
ice = []
for _ in range(n) :
    ice.append(list(map(int, input())))

def dfs(x,y) :
    # 주어진 범위 벗어날 경우
    if x >= n or x < 0 or y >= m or y < 0 :
        return False

    # 만약 음료수가 안채워져 있다면 탐색 시작
    if ice[x][y] == 0 :
        ice[x][y] = 1
        # 상하좌우 모두 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        # 탐색 완료 했으면 true 반환
        return True
    # 탐색할거 없으면 false 반환
    return False

result = 0
# 모든 배열에 관해서 탐색 시작
for i in range(n) :
    for j in range(m) :
        # 반환값이 true면 얼음틀 묶음 있다는 말이므로 +1 해줌!!!
        if dfs(i,j) == True :
            result += 1
print(result)