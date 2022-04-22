s = input()
count0,count1=0,0
if s[0] == '0' :
    count1+= 1
else :
    count0+=1

for i in range(len(s)-1) :
    if s[i]!=s[i+1] :
        if s[i+1] == '0' :
            count1 += 1
        if s[i+1] == '1' :
            count0 += 1
print(min(count0, count1))

#
#     print(s[i-1], s[i], s[i+1])
#     if s[i]=='0' and s[i]!=s[i-1] or s[i]!=s[i+1]:
#         count0+=1
#     elif s[i] == '1' and s[i]!=s[i-1] or s[i]!=s[i+1]:
#         count1+=1
# print(min(count0,count1))