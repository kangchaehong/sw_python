from collections import deque
start = [(1,1),(1,2)]
def search(pos, new_board) :
    next_pos = []
    pos1x, pos1y, pos2x, pos2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4) :
        nextpos1x = pos1x + dx[i]
        nextpos1y = pos1y + dy[i]
        nextpos2x = pos2x + dx[i]
        nextpos2y = pos2y + dy[i]
        if new_board[nextpos1x][nextpos1y] == 0 and new_board[nextpos2x][nextpos2y] == 0 :
            next_pos.append({(nextpos1x, nextpos1y, nextpos2x, nextpos2y)})

    if pos1x == pos2x :
        if new_board[pos1x+1][pos1y] == 0 and new_board[pos1x+1][pos1y+1] == 0:
            for i in [-1,1] :
                if new_board[pos1x+i][pos1y] == 0 and new_board[pos2x+i][pos2y] == 0:
                    next_pos.append({()})

def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]

    for i in range(1,n+1) :
        for j in range(1,n+1):
            new_board[i][j] = board[i-1][j-1]

    q = deque()
    visited = []
    pos = {(1,1),(1,2)}
    q.append((pos,0))
    visited.append(pos)

    while q :
        pos,cost = q.popleft()
        if (n,n) in pos :
            return cost

        for next_pos in search(pos, new_board) :
            if next_pos not in visited :
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0





solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])