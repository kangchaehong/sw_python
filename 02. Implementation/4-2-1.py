n = int(input())
count, count2, count3 = 0,0,0

for h in range(n+1) :
    for m in range(60) :
        for s in range(60) :
            if '3' in str(h)+str(m)+str(s) :
                count += 1
print(count)