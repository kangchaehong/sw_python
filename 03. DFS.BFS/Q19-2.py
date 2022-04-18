# 입력부
n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # +,-,*,/ 순
cal_var = []
# 각 연산자 개수 만큼 배열 재정리
for i in range(len(cal)) :
    for j in range(cal[i]) :
        cal_var.append(i)


# 실행부
def perm(arr, n) :
    result = []
    if len(arr) < n :
        return arr
    if n == 1 :
        for i in arr :
            result.append([i])
    elif n > 1 :
        for i in range(len(arr)) :
            ans = [i for i in arr]
            ans.remove(arr[i]) # 제외시 중복 있는 순열
            for j in perm(ans, n-1):
                result.append([arr[i]]+j)
    return result

def simulate() :
    min_v = 1e9
    max_v = -1e9

    result = perm(cal_var, len(cal_var))
    for cal in result :
        sum = num[0]
        for i in range(len(num)-1) :
            if cal[i] == 0 :
                sum = sum + num[i+1]
            elif cal[i] == 1  :
                sum = sum - num[i+1]
            elif cal[i] == 2 :
                sum = sum * num[i+1]
            elif cal[i] == 3 :
                if sum < 0 :
                    sum = -(-sum // num[i+1])
                else :
                    sum = sum // num[i+1]
        max_v = max(sum, max_v)
        min_v = min(sum, min_v)
    print(int(max_v))
    print(int(min_v))

simulate()