n, m, x, y, k = map(int, input().split())

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
dir = list(map(int, input().split()))


for i in range(k):
    d = dir[i]
    if d == 1:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[2]
        dice[2] = dice[5]
        dice[5] = temp
        if graph[nx][ny] != 0:
            dice[2] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[2]
        print(dice[0])
        x = nx
        y = ny
    elif d == 2:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        temp = dice[0]
        dice[0] = dice[5]
        dice[5] = dice[2]
        dice[2] = dice[4]
        dice[4] = temp
        if graph[nx][ny] != 0:
            dice[2] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[2]
        print(dice[0])
        x = nx
        y = ny
    elif d == 3:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = temp
        if graph[nx][ny] != 0:
            dice[2] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[2]
        print(dice[0])
        x = nx
        y = ny
    elif d == 4:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = temp
        if graph[nx][ny] != 0:
            dice[2] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[2]
        print(dice[0])
        x = nx
        y = ny