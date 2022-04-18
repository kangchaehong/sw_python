n = input()
alp = []
num = 0
for i in range(len(n)) :
    if n[i].isalpha() :
        alp.append(n[i])
    else :
        num += int(n[i])
alp.sort()

if num != 0 :
    alp.append(str(num))

print(''.join(alp))