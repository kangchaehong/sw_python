n = int(input())

number = list(map(int,input().split()))
sign = list((map(int,input().split())))
new_sign = [] * (n-1)
real_result = []
# 최소, 최대 값
max_v = -1e9
min_v = 1e9
result = number[0]

def perm(sign) :
    sum = 0
    for i in range(4) :
        sum += sign[i]
        if sign[i] != 0 :
            new_sign.append(i)

    # for i in range(sum) :


    return new_sign


new_sign = perm(sign)
for i in range(len(new_sign)) :
    if new_sign[i] == 0 :
        result = int(result + number[i+1])
    elif new_sign[i] == 1 :
        result = int(result - number[i+1])
    elif new_sign[i] == 2 :
        result = int(result * number[i+1])
    elif new_sign[i] == 3 :
        result = int(result / number[i+1])

max_v = max(result, max_v)
min_v = min(result, min_v)

print(max_v, min_v, sep="\n")
