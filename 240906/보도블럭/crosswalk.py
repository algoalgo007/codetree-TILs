n, l = map(int, input().split())
graph = []
ans = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]

for i in range(n):
    flag = True
    for j in range(1, n):
        if abs(graph[i][j] - graph[i][j-1]) >= 2:
            flag = False
            break
        else:
            # 경사로 오른쪽 -> 왼쪽
            if graph[i][j] < graph[i][j-1]:
                if j + l <= n:
                    road = set()
                    arr = []
                    for k in range(j, j + l):
                        road.add(graph[i][k])
                        arr.append((i, k))
                        if visited[i][k] == True:
                            flag = False
                            break
                    if len(road) >= 2:
                        flag = False
                        break
                    if flag:
                        for k in range(len(arr)):
                            x, y = arr[k]
                            visited[x][y] = True
                else:
                    flag = False
                    break
            # 경사로 왼쪽 -> 오른쪽
            elif graph[i][j] > graph[i][j-1]:
                if j - l >= 0:
                    road = set()
                    arr = []
                    for k in range(j-1,j-l-1,-1):
                        road.add(graph[i][k])
                        arr.append((i, k))
                        if visited[i][k] == True:
                            flag = False
                            break
                    if len(road) >= 2:
                        flag = False
                        break
                    if flag:
                        for k in range(len(arr)):
                            x, y = arr[k]
                            visited[x][y] = True
                else:
                    flag = False
                    break
    if flag:
        ans += 1

visited = [[False] * n for _ in range(n)]

for j in range(n):
    flag = True
    for i in range(1, n):
        if abs(graph[i][j] - graph[i-1][j]) >= 2:
            flag = False
            break
        else:
            # 경사로 위 -> 아래
            if graph[i][j] > graph[i-1][j]:
                if i - l >= 0:
                    road = set()
                    arr = []
                    for k in range(i-1, i-1-l, -1):
                        road.add(graph[k][j])
                        arr.append((k, j))
                        if visited[k][j] == True:
                            flag = False
                            break
                    if len(road) >= 2:
                        flag = False
                        break
                    if flag:
                        for k in range(len(arr)):
                            x, y = arr[k]
                            visited[x][y] = True
                else:
                    flag = False
                    break
            # 경사로 아래 -> 위
            if graph[i][j] < graph[i-1][j]:
                if i + l <= n:
                    road = set()
                    arr = []
                    for k in range(i, i + l):
                        road.add(graph[k][j])
                        arr.append((k, j))
                        if visited[k][j] == True:
                            flag = False
                            break
                    if len(road) >= 2:
                        flag = False
                        break
                    if flag:
                        for k in range(len(arr)):
                            x, y = arr[k]
                            visited[x][y] = True
                else:
                    flag = False
                    break
    if flag:
        ans += 1
print(ans)