n, k = map(int, input().split())

count = 0

# while n != 1 :
#     if n % k == 0 :
#         n /= k
#     else :
#         n -= 1
#     count += 1

## 한번에 빼는 방법은??
# target 잡고 target까지 한번에 빼기
while True :
    target = (n // k) * k
    count += (n-target)
    n = target

    if n < k :
        break

    count += 1
    n //= k
count += (n-1)
print(count)

    # if n%k != 0 :
    #     target = (n // k) * k
    #     count += n - target
    #     n = target
    #
    # else :
    #     n //= k
    #     count += 1
    #
    # if n == 1 :
    #     break
