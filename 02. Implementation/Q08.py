a = input()
s = []
n = 0
for i in range(len(a)) :
    if a[i].isdigit() :
        n += int(a[i])
    else :
        s.append(a[i])
s.sort()

for i in s :
    print(i, end ='')
print(n)

# print(''.join(s))