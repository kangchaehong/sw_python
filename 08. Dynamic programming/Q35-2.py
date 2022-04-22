n = int(input())
val2, val3, val5 = 2,3,5
cnt2, cnt3, cnt5 = 0,0,0
d = [1] * n

for i in range(1,n):
    d[i] = min(val2, val3, val5)
    if d[i] == val2 :
        cnt2 += 1
        val2 = d[cnt2] *2
    if d[i] == val3 :
        cnt3 += 1
        val3 = d[cnt3] *3
    if d[i] == val5 :
        cnt5 += 1
        val5 = d[cnt5] *5
print(d[n-1])