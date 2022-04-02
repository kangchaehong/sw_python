a = input()
left = 0
right = 0

for i in range(len(a)//2) :
    left += int(a[i])
    right += int(a[-(i+1)])

if left == right :
    print("LUCKY")
else :
    print("READY")