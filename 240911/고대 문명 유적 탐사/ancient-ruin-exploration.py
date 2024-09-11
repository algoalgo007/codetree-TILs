import copy
from collections import deque

k, m = map(int, input().split())
graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
arti = list(map(int, input().split()))
arti = arti[::-1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
array = []
pos = []

def bfs(graph, visited, x, y, flag):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    val = graph[x][y]
    count = 0
    tt = []
    while q:
        x, y = q.popleft()
        count += 1
        tt.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if graph[nx][ny] == val and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

    if flag and len(tt) >= 3:
        for i in range(len(tt)):
            pos.append(tt[i])
    return count

def turn90(x, y, cnt, flag):
    tempGraph = copy.deepcopy(graph)

    tempGraph[x-1][y-1] = graph[x+1][y-1]
    tempGraph[x-1][y] = graph[x][y-1]
    tempGraph[x-1][y+1] = graph[x-1][y-1]

    tempGraph[x][y-1] = graph[x+1][y]
    tempGraph[x][y+1] = graph[x-1][y]

    tempGraph[x+1][y-1] = graph[x+1][y+1]
    tempGraph[x+1][y] = graph[x][y+1]
    tempGraph[x+1][y+1] = graph[x-1][y+1]

    count = 0
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                temp = bfs(tempGraph, visited, i, j, flag)
                if temp >= 3:
                    count += temp
    if count != 0:
        array.append((count, cnt, x, y))

    if flag:
        for i in range(5):
            for j in range(5):
                graph[i][j] = tempGraph[i][j]

def turn180(x, y, cnt, flag):
    tempGraph = copy.deepcopy(graph)

    tempGraph[x-1][y-1] = graph[x+1][y+1]
    tempGraph[x-1][y] = graph[x+1][y]
    tempGraph[x-1][y+1] = graph[x+1][y-1]

    tempGraph[x][y-1] = graph[x][y+1]
    tempGraph[x][y+1] = graph[x][y-1]

    tempGraph[x+1][y-1] = graph[x-1][y+1]
    tempGraph[x+1][y] = graph[x-1][y]
    tempGraph[x+1][y+1] = graph[x-1][y-1]

    count = 0
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                temp = bfs(tempGraph, visited, i, j, flag)
                if temp >= 3:
                    count += temp
    if count != 0:
        array.append((count, cnt, x, y))

    if flag:
        for i in range(5):
            for j in range(5):
                graph[i][j] = tempGraph[i][j]

def turn270(x, y, cnt, flag):
    tempGraph = copy.deepcopy(graph)

    tempGraph[x-1][y-1] = graph[x-1][y+1]
    tempGraph[x-1][y] = graph[x][y+1]
    tempGraph[x-1][y+1] = graph[x+1][y+1]

    tempGraph[x][y-1] = graph[x-1][y]
    tempGraph[x][y+1] = graph[x+1][y]

    tempGraph[x+1][y-1] = graph[x-1][y-1]
    tempGraph[x+1][y] = graph[x][y-1]
    tempGraph[x+1][y+1] = graph[x+1][y-1]

    count = 0
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                temp = bfs(tempGraph, visited, i, j, flag)
                if temp >= 3:
                    count += temp
    if count != 0:
        array.append((count, cnt, x, y))

    if flag:
        for i in range(5):
            for j in range(5):
                graph[i][j] = tempGraph[i][j]

for _ in range(k):
    ans = 0
    array = []
    pos = []
    for i in range(1, 4):
        for j in range(1, 4):
            turn90(i, j, 1, False)
            turn180(i, j, 2, False)
            turn270(i, j, 3, False)

    if len(array) == 0:
        continue
    array.sort(key = lambda x: (-x[0], x[1], x[3], x[2]))
    value, num, x, y = array[0]
    if num == 1: 
        turn90(x, y, 1, True)
    elif num == 2:
        turn180(x, y, 2, True)
    elif num == 3:
        turn270(x, y, 3, True)
    pos.sort(key = lambda x: (x[1], -x[0]))
    while True:
        for i in range(len(pos)):
            x, y = pos[i]
            ans += 1
            graph[x][y] = arti.pop()
        pos = []
        visited = [[False] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                bfs(graph, visited, i, j, True)
        if len(pos) == 0:
            break
        pos.sort(key = lambda x: (x[1], -x[0]))
    print(ans, end=" ")