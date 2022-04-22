def solution(food_times, k) :
    n = len(food_times)
    foods = []
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()

    pretime = 0
    for i, food in enumerate(foods) :
        diff = food[0]-pretime
        spend = diff * n
        if spend <= k :
            k -= spend
            pretime = food[0]
        else :
            k %= n
            sublist = sorted(foods[i:], key=lambda x: x[1])
            return sublist[k][1]
        n-=1
    return -1


food_times = [3, 1, 2]
k = 5
solution(food_times, k)