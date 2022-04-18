s = input()
result = int(s[0])
for i in range(1,len(s)) :
    if s[i-1] == '0' or s[i-1] == '1' :
        result = result + int(s[i])
    else :
        result = result * int(s[i])
print(result)