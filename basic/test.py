miro = []
for i in range(10) :
    a = list(map(int, input().split()))
    miro.append(a)

i = 1
j = 1

while True :
    miro[i][j] = 9
    if miro[i][j+1] == 0:
        j +=1
    elif miro[i][j+1] == 1 and miro[i+1][j] == 0 :
        i+=1
    elif miro[i+1][j] == 2 :
        i+=1
        miro[i][j] = 9
        break
    elif miro[i][j+1] == 2:
        j += 1
        miro[i][j] = 9
        break
    elif miro[i][j+1] == 1 and miro[i+1][j] == 1 :
        miro[i][j] = 9
        break
    elif i == 8 and j == 8 :
        miro[i][j] = 9
        break

for i in range(10) :
    for j in range(10) :
        print(miro[i][j], end=' ')
    print()

# a,b,c = map(int,input().split())
# d = 1
# while d%a != 0 or d%b !=0 or d%c != 0 :
#     d += 1
# print(d)

# a = int(input())
# b = input().split()
#
# for i in range(a-1, -1, -1) :
#     print(b[i], end=' ')

# d = []
# for i in range(19) :
#     ds = list(map(int, input().split()))
#     d.append(ds)
