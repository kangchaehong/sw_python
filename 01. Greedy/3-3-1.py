n, m = map(int, input().split())
result = 0
for i in range(n) :
    card = (list(map(int, input().split())))
    # if minv < min(card[i]) :
    #     minv = min(card[i])
    minv = min(card)
    minv = max(minv, result)

print(result)