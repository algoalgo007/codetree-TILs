import copy
from collections import deque

k, m = map(int, input().split())
graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
artifact = list(map(int, input().split()))
artifact = artifact[::-1]
visited = [[False] * 5 for _ in range(5)]
bag = []
ans = 0
move = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
    return cnt

def bfs2(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    temp = []
    cnt = 0
    while q:
        x, y = q.popleft()
        temp.append((x, y))
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
    if len(temp) >= 3:
        for tx, ty in temp:
            move.append((tx, ty))
    return cnt

def rotate90(x, y, flag, visited):
    visited = [[False] * 5 for _ in range(5)]
    cGraph = copy.deepcopy(graph)
    cGraph[x-1][y-1] = graph[x+1][y-1]
    cGraph[x-1][y] = graph[x][y-1]
    cGraph[x-1][y+1] = graph[x-1][y-1]
    cGraph[x][y-1] = graph[x+1][y]
    cGraph[x][y+1] = graph[x-1][y]
    cGraph[x+1][y-1] = graph[x+1][y+1]
    cGraph[x+1][y] = graph[x][y+1]
    cGraph[x+1][y+1] = graph[x-1][y+1]
    if flag:
        cnt = 0
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    result = bfs(i, j, cGraph, visited)
                    if result >= 3:
                        cnt += result
        if cnt != 0:
            bag.append((cnt, 0, x, y))
    else:
        for i in range(5):
            for j in range(5):
                graph[i][j] = cGraph[i][j]

def rotate180(x, y, flag, visited):
    visited = [[False] * 5 for _ in range(5)]
    cGraph = copy.deepcopy(graph)
    cGraph[x-1][y-1] = graph[x+1][y+1]
    cGraph[x-1][y] = graph[x+1][y]
    cGraph[x-1][y+1] = graph[x+1][y-1]
    cGraph[x][y-1] = graph[x][y+1]
    cGraph[x][y+1] = graph[x][y-1]
    cGraph[x+1][y-1] = graph[x-1][y+1]
    cGraph[x+1][y] = graph[x-1][y]
    cGraph[x+1][y+1] = graph[x-1][y-1]
    if flag:
        cnt = 0
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    result = bfs(i, j, cGraph, visited)
                    if result >= 3:
                        cnt += result
        if cnt != 0:
            bag.append((cnt, 1, x, y))
    else:
        for i in range(5):
            for j in range(5):
                graph[i][j] = cGraph[i][j]


def rotate270(x, y, flag, visited):
    visited = [[False] * 5 for _ in range(5)]
    cGraph = copy.deepcopy(graph)
    cGraph[x-1][y-1] = graph[x-1][y+1]
    cGraph[x-1][y] = graph[x][y+1]
    cGraph[x-1][y+1] = graph[x+1][y+1]
    cGraph[x][y-1] = graph[x-1][y]
    cGraph[x][y+1] = graph[x+1][y]
    cGraph[x+1][y-1] = graph[x-1][y-1]
    cGraph[x+1][y] = graph[x][y-1]
    cGraph[x+1][y+1] = graph[x+1][y-1]
    if flag:
        cnt = 0
        for i in range(5):
            for j in range(5):
                result = bfs(i, j, cGraph, visited)
                if result >= 3:
                    cnt += result
        if cnt != 0:
            bag.append((cnt, 2, x, y))
    else:
        for i in range(5):
            for j in range(5):
                graph[i][j] = cGraph[i][j]

for _ in range(k):
    bag = []
    move = []
    for i in range(1, 4):
        for j in range(1, 4):
            rotate90(i, j, True, visited)
            rotate180(i, j, True, visited)
            rotate270(i, j, True, visited)
    if len(bag) == 0:
        break
    else:
        bag.sort(key = lambda x: (-x[0], x[1], x[3], x[2]))
        num, method, xpos, ypos = bag[0]
        ans += num
        if method == 0:
            rotate90(xpos, ypos, False, visited)
        elif method == 1:
            rotate180(xpos, ypos, False, visited)
        else:
            rotate270(xpos, ypos, False, visited)
        visited = [[False] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    bfs2(i, j, graph, visited)
        move.sort(key = lambda x : (x[1], -x[0]))
        for tx, ty in move:
            graph[tx][ty] = artifact.pop()
        visited = [[False] * 5 for _ in range(5)]
        while True:
            temp = 0
            move = []
            for i in range(5):
                for j in range(5):
                    if not visited[i][j]:
                        temp2 = bfs2(i, j, graph, visited)
                        if temp2 >= 3:
                            temp += temp2
            if temp == 0:
                break
            else:
                ans += temp
                move.sort(key=lambda x: (x[1], -x[0]))
                visited = [[False] * 5 for _ in range(5)]
                for tx, ty in move:
                    graph[tx][ty] = artifact.pop()
    print(ans, end=" ")
    ans = 0