a = input()
result = 0

for i in range(len(a)) :
    # if result == 0 or result == 1 :
    num = int(a[i])
    if result <= 1 or  num <= 1 :
        result += num
    else :
        result *= num

print(result)