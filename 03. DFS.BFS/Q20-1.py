from collections import deque
from itertools import combinations
import copy

n = int(input())
graph = []
teacher = []
blank = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == "X":
            blank.append((i, j))


def bfs():  # 학생 찾으면 False 반환
    q = deque(teacher)
    test_graph = copy.deepcopy(graph)
    while q:
        x, y = q.popleft()
        for i in range(4):
            temp_x, temp_y = x, y
            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if test_graph[nx][ny] == 'X':
                        test_graph[nx][ny] = 'T'
                    elif test_graph[nx][ny] == 'S':
                        return False
                    elif test_graph[nx][ny] == 'O':
                        break
                    temp_x, temp_y = nx, ny
                else:
                    break
    return True

check = False
for data in list(combinations(blank, 3)):
    for x, y in data:
        graph[x][y] = 'O'
    if bfs():
        check = True
        break
    for x, y in data:
        graph[x][y] = 'X'

if check:
    print("YES")
else:
    print("NO")