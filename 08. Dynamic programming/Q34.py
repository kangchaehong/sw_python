n = int(input())
s = list(map(int, input().split()))

d = [1] * n
# d.append(s[0])
# for i in range(1, n) :
#     if i == n-1 :
#         if d[-1] >= s[i] :
#             d.append(s[i])
#             continue
#     if d[-1] >= s[i] and s[i] >= s[i+1] :
#         d.append(s[i])
#
# print(n-len(d))

for i in range(n-1) :
    for j in range(i+1, n) :
        if s[i] > s[j] :
            d[j] = max(d[j], d[i]+1)
print(n- max(d))