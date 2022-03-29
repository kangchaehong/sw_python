N, K = map(int, input().split())
cnt = 0
while N!=1 :
    if N % K != 0 :
        cnt += 1
        N -= 1
    elif N % K == 0 :
        cnt += 1
        N /= K
print(cnt)

# example
# 가능한 최대한 많이 나누는 것이 최적의 해 보장!!
# while 문 한번에 무조건 // 수행하므로 위의 해결법보다 효과적으로 값 감소 가능!!
#
# while True :
#     # N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
#     target = (N//K) * K
#     cnt += (N-target)
#     N = target
#     # 더 이상 나눌 수 없을때 반복문 탈출
#     if K > N :
#         break
#     cnt += 1
#     N //= K
#
# cnt += N-1
# print(cnt)
#
