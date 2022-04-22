def rotate(rkey, keylen) :
    new_key = [[0]*keylen for _ in range(keylen)]
    for i in range(keylen) :
        for j in range(keylen) :
            new_key[i][j] = rkey[keylen-j-1][i]
    return new_key

def check(lock) :
    start_lock = len(lock) // 3
    for i in range(start_lock, 2*start_lock) :
        for j in range(start_lock, 2*start_lock) :
            if lock[i][j] !=1 :
                return False
    return True

def solution(key, lock) :
    lock_len = len(lock)
    k_len = len(key)
    new_lock = [[0]*(lock_len*3) for _ in range(lock_len*3)]

    # 확장된 lock 초기화
    for i in range(lock_len) :
        for j in range(lock_len) :
            new_lock[i+lock_len][j+lock_len] = lock[i][j]

    for i in range((lock_len*3)-k_len+1):
        for j in range((lock_len*3)-k_len+1) :
            for k in range(4) :
                key = rotate(key, k_len)
                for a in range(k_len) :
                    for b in range(k_len) :
                        new_lock[i+a][j+b] += key[a][b]
                if check(new_lock) :
                    return True
                for a in range(k_len):
                    for b in range(k_len):
                        new_lock[i + a][j + b] -= key[a][b]
    return False



key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# rotate(key)
print(solution(key, lock))