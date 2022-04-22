def cal_diff(t1,t2) :
    team1 = 0
    team2 = 0
    for i in range(len(t1)):
        for j in range(len(t1)) :
            team1 += team[t1[i]][t1[j]]
            team2 += team[t2[i]][t2[j]]
    return abs(team1-team2)

def bfs(team1, idx, start,n) :
    global answer
    if idx == n//2 :
        team2 = []
        for i in range(n):
            if i not in team1 :
                team2.append(i)
        diff = cal_diff(team1, team2)
        answer = min(answer, diff)
        return

    for i in range(start, n) :
        if i not in team1 :
            team1.append(i)
            bfs(team1, idx+1, start+1,n)
            team1.remove(i)

if __name__=="__main__" :
    n = int(input())
    team = [list(map(int, input().split())) for _ in range(n)]
    # for i in range(n):
    #     team.append(list(map(int, input().split())))
    # temp = [i for i in range(n)]
    answer = 1e9

    bfs([],0,0,n)
    print(answer)