food_times = [3, 1, 2]
k = 5
new_foods = []
result = []
def solution(food_times, k) :
    for i in range(len(food_times)) :
        new_foods.append([food_times[i], i])

    new_foods.sort(key=lambda x : x[0])
    foodlen = len(food_times)
    for i in range(len(food_times)-1) :
        sub = (new_foods[i + 1][0] - new_foods[i][0])
        if sub != 0 :
            print('sub', sub)
            diff = foodlen * sub
            print('diff', diff)
            print('k',k)
            if k - diff < 0:
                print('nf', new_foods)
                for i in range(len(food_times)):
                    if new_foods[i][0] != 0:
                        result.append(new_foods[i][1])
                k %= foodlen
                return result
            k -= diff
            for j in range(i, len(food_times)) :
                new_foods[j][0] -= sub
            foodlen -= 1

        if foodlen <= 0 :
            return -1




print(solution(food_times, k))