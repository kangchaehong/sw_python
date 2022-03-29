a, b = map(int, input().split())
result = 0

while True :
    target = (a // b) * a
    result += a-target

    if a < target :
        break

    result += 1
    a //= b

result += a-1
print(result)