a = input()
b = []
sum = 0

for i in a :
    if 48 <= ord(i) and ord(i) <= 57 :
        sum += int(i)
    else :
        b.append(i)

    # if i.isalpha():
    #     b.append(i)
    # else :
    #     sum += int(i)

b.sort()
#### 숫자 없을 경우 예외처리 필요함!!
if sum != 0 :
    b.append(str(sum))

# for j in b :
#     print(j, end ='')

print(''.join(b))