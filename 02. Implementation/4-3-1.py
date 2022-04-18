n = input()
count = 0
moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
x = (ord(n[0])-97) + 1
y = int(n[1])

for move in moves :
    nx = x + move[0]
    ny = y + move[1]

    if nx > 0 and nx <= 8 and ny > 0 and ny <= 8 :
        count += 1

print(count)