s = input()
cnt0, cnt1 = 0,0

if s[0] == '0' :
    cnt0 += 1
else :
    cnt1 += 1

for i in range(1,len(s)) :
    if s[i-1] == '0' and s[i] == '1' :
        cnt1+=1
    if s[i-1] == '1' and s[i] == '0' :
        cnt0+=1
print(min(cnt0, cnt1))
