# a = input()
# sum = 0
# for i in range(len(a)) :
#     if (sum + int(a[i])) >= (sum*int(a[i])) :
#         sum +=int(a[i])
#     else :
#         sum *= int(a[i])
# print(sum)

# example
a = input()
result = int(a[0])

for i in range(1, len(a)) :
    num = int(a[i])
    if num <=1 or result <=1 :
        result += num
    else :
        result *= num
print(result)