n = input()
l = int(len(n) / 2)
left, right = 0,0
for i in range(l) :
    left += int(n[i])
    right += int(n[l+i])

if left == right :
    print('LUCKY')
else :
    print('READY')