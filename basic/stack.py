###Stack

from sys import stdin

n = int(stdin.readline())
q = []
for i in range(n) :
    # # n = int(input())
    com = stdin.readline().split()
    if com[0] == 'push' :
        q.append(com[1])
    elif com[0] == 'pop' :
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
    elif com[0] == 'top' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[-1])
