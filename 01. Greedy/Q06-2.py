food_times = [5, 0, 3, 3, 1]
k= 9
result = 1

a = [3,5,1,6,5,3]
k1 = 20

# food_times = [4,2,3,6,7,1,5,8]
# k=16

def solution(food_times, k) :
    foods = []
    pretime = 0
    n = len(food_times)
    for i in range(n) :
        foods.append((food_times, i+1))
    food_times.sort()

    for i, food in enumerate(foods) :
        diff = food[0] - pretime
        if diff != 0 :
            spend = diff * n
            if spend <= k :
                k -= spend
                pretime = foods[0]
            else :
                k %= n
                sublist = sorted(foods[i:], key = lambda x :x[1])
                return sublist[k][1]
        n-=1
    return -1

print(solution(food_times, k))