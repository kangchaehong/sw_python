from sys import stdin

n = int(stdin.readline())
q = []
for i in range(n) :
    com = stdin.readline().split()
    if com[0] == 'push_front' :
        # q = list(com[1]) + q
        q.insert(0,com[1])
    elif com[0] == 'push_back' :
        q.append(com[1])
    elif com[0] == 'pop_front' :
        if len(q)==0 :
            print('-1')
        else :
            print(q.pop(0))
    elif com[0] == 'pop_back' :
        if len(q)==0 :
            print('-1')
        else :
            print(q.pop(-1))
    elif com[0] == 'size' :
        print(len(q))
    elif com[0] == 'empty':
        if len(q) == 0 :
            print('1')
        else :
            print('0')
    elif com[0] == 'front' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[0])
    elif com[0] == 'back' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[-1])