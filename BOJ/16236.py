if __name__ == "__main__" :
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]
    next_sea = [[0]*n for _ in range(n)]
    nx = [0,0,-1,1]
    ny = [-1,1,0,0]

    print(next_sea)