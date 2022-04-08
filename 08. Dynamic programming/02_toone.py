n = int(input())
cnt = 0
while n != 1 :

    if n % 5 == 0 :
        n /= 5
    if n % 3 == 0 :
        n /= 3
    if n % 2 == 0 :
        n /= 2
    n -= 1
    cnt +=1
print(cnt)


# dp
n = int(input())
d = [0] * 30001

for i in range(2, n+1) :
    d[i] = d[i-1] + 1

    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5]+1)

print(d[n])
