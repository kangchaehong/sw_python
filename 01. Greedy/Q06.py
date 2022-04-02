food_times = [3,1,2]
k = 5

def live(food_times, k) :
    cnt = 0
    p = 0

    while True :
        p %= 3
        if food_times[p] == 0 :
            p += 1
            continue
        else :
            food_times[p] -= 1
        if cnt == k :
            return p+1
        if sum(food_times) <= 0 :
            return -1
        print(food_times)
        cnt += 1
        p += 1

print(live(food_times, k))
