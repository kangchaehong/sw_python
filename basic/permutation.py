def permuation() :
    a = int(input())
    b = []
    used = [0]*a
    for i in range(a) :
        b.append(i+1)

    def generate(chosen, used) :
        if len(chosen) == a :
            for i in chosen :
                print(i)
            return

        for i in range(len(b)):
            if not used[i] :
                chosen.append(b[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([],used)



if __name__ == '__main__':
    permuation()