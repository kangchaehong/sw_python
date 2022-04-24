n, m, k = map(int, input().split())
s2d2 = [list(map(int,input().split())) for _ in range(n)]
treelist = [list(map(int, input().split())) for _ in range(m)]

eat = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for x,y,old in treelist :
    tree[x-1][y-1].append(old)


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(k) :
    # 봄, 여름 (여름 나중에 처리!!)
    for i in range(n) :
        for j in range(n) :
            dieindx = -1
            temp = tree[i][j]
            if temp :
                temp.sort()
                for k in range(len(temp)) :
                    if eat[i][j] >= temp[k] :
                        eat[i][j] -= temp[k]
                        temp[k] += 1
                    else :
                        dieindx = k
                        # nu = temp[k] // 2
                        # dietree.append([i,j,temp[k], nu])
                        break
                if dieindx != -1 :
                    tree[i][j] = tree[i][j][:k]
                    for c in range(dieindx, len(temp)) :
                        eat[i][j] += (temp[c] // 2)
                # for dix,diy,dio,nu in dietree :
                #     tree[dix][diy].remove(dio)
                #     eat[i][j] += nu

    # 가을
    for i in range(n) :
        for j in range(n) :
            temp = tree[i][j]
            for k in range(len(temp)) :
                if temp[k] % 5 == 0 :
                    for a in range(8) :
                        nx = i + dx[a]
                        ny = j + dy[a]
                        if nx>=0 and nx <n and ny>=0 and ny < n :
                            tree[nx][ny].append(1)

    # 겨울
    for i in range(n) :
        for j in range(n) :
            eat[i][j] += s2d2[i][j]

total = 0
for i in range(n) :
    for j in range(n) :
        total += len(tree[i][j])

print(total)




