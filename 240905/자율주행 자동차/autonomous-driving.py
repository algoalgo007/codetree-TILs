n, m = map(int,input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

turn_cnt = 0

def turn_left(d):
    if d == 0:
        return 3
    else:
        return d - 1

def turn_right(d):
    if d == 3:
        return 0
    else:
        return d + 1
    
graph[x][y] = 2
ans = 1

while True:
    if turn_cnt >= 5:
        d = turn_right(d)
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 2:
            x = nx
            y = ny
            turn_cnt = 0
        else:
            break
    d = turn_left(d)
    turn_cnt += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if graph[nx][ny] == 0:
        turn_cnt = 0
        x = nx
        y = ny
        ans += 1
        graph[x][y] = 2

print(ans)