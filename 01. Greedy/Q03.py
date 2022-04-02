a = input()
cnt = 1

for i in range(1,len(a)) :
    if a[i-1] == a[i] :
        pass
    else :
        cnt += 1

cnt = int(cnt / 2)
print(cnt)


# example
# 0에서 1로 모두 바꾸는 경우 or 1에서 0으로 모두 바꾸는 경우

# a = input()
# result0 = 0
# result1 = 0
#
# if a[0] == '1' :
#     result0 += 1
# else :
#     result1 += 1
#
# for i in range(len(a)-1) :
#     if a[i] != a[i+1] :
#         if a[i+1] == '1' :
#             result0 += 1
#         else :
#             result1 +=1
#
# print(min(result0, result1))
