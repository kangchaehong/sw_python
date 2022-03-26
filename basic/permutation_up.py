def main():
    a = int(input())
    n = list(map(int,input().split()))
    used = [0] * a
    res_arr = []

    def gen(check, used, res_arr) :

        if len(check) == a :
            res = 0
            for num in range(a-1) :
                res = res + abs(check[num]-check[num+1])
            res_arr.append(res)
            return

        for i in range(a) :
            if not used[i] :
                check.append(n[i])
                used[i] = 1
                gen(check, used, res_arr)
                used[i] = 0
                check.pop()

    gen([],used, res_arr)
    print(res_arr)
    print(max(res_arr))


if __name__ == '__main__' :
    main()


