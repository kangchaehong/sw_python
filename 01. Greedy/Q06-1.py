def solution(food_times, k) :
    foods =[]
    n = len(food_times)
    for i in range(n) :
        foods.append((food_times[i], i+1))

    foods.sort()

    pretime = 0
    for i, food in enumerate(foods) :
        # print(i, food[0])
        diff = food[0] - pretime
        if diff != 0 :
            spend = diff * n
            if spend <= k :
                k -= spend
                pretime = food[0]
            else :
                k %= n
                sublist=sorted(foods[i:], key=lambda x : x[1] )
                return sublist[k][1]
        n-=1
    return -1

a = [3,5,1,6,5,3]
k = 20
print(solution(a,k))