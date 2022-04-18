s = input()
# 전부 0으로 바뀌는 경우, 1로 바뀌는 경우
cnt0, cnt1 = 0,0

# 첫번째 원소 처리
if s[0] == '1' : # 첫번째 원소 1이면
    cnt0 += 1 # 0으로 바뀌는 경우 추가
else :
    cnt1 += 1

for i in range(len(s)-1) :
    if s[i] != s[i+1] :
        if s[i+1] == '0' :
            cnt1 += 1
        else :
            cnt0 += 1
    print(cnt0, cnt1)
print(min(cnt0, cnt1))