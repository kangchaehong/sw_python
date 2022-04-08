n = int(input())

d = [0] * n
d[0] = 1
idx2, idx3, idx5 = 0,0,0
val2, val3, val5 = 2,3,5

# 모두 if로 걸어줘야함! 중복된 수 나올 경우 if문에 들어가게 하기 위해서!!
for i in range(1,n) :
    d[i] = min(val2,val3,val5)
    if d[i] == val2 :
        idx2 += 1
        val2 = d[idx2] * 2
    if d[i] == val3 :
        idx3 += 1
        val3 = d[idx3] * 3
    if d[i] == val5 :
        idx5 += 1
        val5 = d[idx5] * 5

print(d[n-1])