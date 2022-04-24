n, m = int(input())
basket = [list(map(int, input().split())) for _ in range(n)]
move=[list(map(int, input().split())) for _ in range(m)]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

cloud = [(n,1), (n,2),(n-1,1),(n-1,2)]
