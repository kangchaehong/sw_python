from sys import stdin
## Queue

def main() :
    n = int(stdin.readline())
    q = []
    for i in range(n):
        com = stdin.readline().split()
        if com[0] == 'push':
            q.append(com[1])
        elif com[0] == 'pop':
            if len(q) == 0:
                print('-1')
            else:
                print(q.pop(0))
        elif com[0] == 'size':
            print(len(q))
        elif com[0] == 'empty':
            if len(q) == 0:
                print('1')
            else:
                print('0')
        elif com[0] == 'front':
            if len(q) == 0:
                print('-1')
            else:
                print(q[0])
        elif com[0] == 'back':
            if len(q) == 0:
                print('-1')
            else:
                print(q[-1])

if __name__ == '__main__':
    main()
# print_hi('PyCharm')
# q = queue.Queue()
    # n = int(input())
