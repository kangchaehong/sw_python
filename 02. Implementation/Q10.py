def rotate(list) :
    a = len(list)
    b = len(list[0])
    result = [[0]*a for _ in range(b)]

    for i in range(a) :
        for j in range(b) :
            result[j][a-i-1] = list[i][j]

    return result

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2) :
        for j in range(lock_length, lock_length*2) :
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n) :
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]

    # 모든 회전 방향으로 돌리기
    for rotation in range(4) :
        key = rotate(key)
        # 최대 확인 가로 세로 개수는 6임!!
        for x in range(n*2) :
            for y in range(n*2) :
                # 왼쪾서부터 오른쪽으로 한번씩 끼워보기
                for a in range(m) :
                    for b in range(m) :
                        new_lock[x+a][y+b] += key[a][b]
                # 맞는지 확인
                if check(new_lock) == True :
                    return True
                # 다시 자물쇠 값 뺴기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
    return False



key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key, lock))