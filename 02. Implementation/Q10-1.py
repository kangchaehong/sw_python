
def solution(key, lock) :
    locklen = len(lock) - 1
    keylen = len(key)
    newlen = len(lock) + ((len(key) - 1) * 2)
    new_array = [[0]*newlen for _ in range(newlen)]

    for i in range(len(lock)) :
        for j in range(len(lock)) :
            new_array[locklen+i][locklen+j] = lock[i][j]

    for i in range(4):
        key = rotate(key)
        for x in range(locklen+keylen) :
            for y in range(locklen+keylen) :
                for j in range(keylen) :
                    for k in range(keylen) :
                        new_array[x+j][y+k] += key[j][k]
                if check(new_array, locklen+1) :
                    return True
                for j in range(keylen) :
                    for k in range(keylen) :
                        new_array[x+j][y+k] -= key[j][k]
    return False

def check(array, locklen) :
    lenarray = (len(array) // 2) - 1
    for i in range(lenarray, lenarray+locklen ) :
        for j in range(lenarray, lenarray+locklen) :
            if array[i][j] != 1 :
                return False
    return True

def rotate(key) :
    key_len = len(key)
    result = [[0]*key_len for _ in range(key_len)]
    for i in range(key_len) :
        for j in range(key_len) :
            result[j][key_len-i-1] = key[i][j]
    return result




key = [[0,0,0],[1,0,0],[0,1,1]]
# key = [[0,0],[1,0]]
# lock = [[1,0],[1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key, lock))