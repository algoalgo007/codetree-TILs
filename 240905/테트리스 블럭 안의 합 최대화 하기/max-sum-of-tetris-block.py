ans = []
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y, dx, dy):
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or  ny < 0 or nx >= n or ny >= m:
            return
        temp += graph[nx][ny]
    ans.append(temp)

for i in range(n):
    for j in range(m):
        bfs(i, j, [0, 0, 0, 0], [0, 1, 2, 3])
        bfs(i, j, [0, 1, 2, 3], [0, 0, 0, 0])
        bfs(i, j, [0, 0, 1, 1], [0, 1, 0, 1])
        bfs(i, j, [0, 1, 2, 2], [0, 0, 0, 1])
        bfs(i, j, [0, 0, 0, 1], [0, 1, 2, 0])
        bfs(i, j, [0, 0, 1, 2], [0, 1, 1, 1])
        bfs(i, j, [0, 1, 1, 1], [0, 0, -1, -2])
        bfs(i, j, [0, 0, -1, -2], [0, 1, 1, 1])
        bfs(i, j, [0, 1, 1, 1], [0, 0, 1, 2])
        bfs(i, j, [0, 0, 1, 2], [0, 1, 0, 0])
        bfs(i, j, [0, 0, 0, 1], [0, 1, 2, 2])
        bfs(i, j, [0, 1, 1, 2], [0, 0, 1, 1])
        bfs(i, j, [0, 0, -1, -1], [0, 1, 1, 2])
        bfs(i, j, [0, -1, -1, -2], [0, 0, 1, 1])
        bfs(i, j, [0, 0, 1, 1], [0, 1, 1, 2])
        bfs(i, j, [0, 1, 1, 2], [0, 0, 1, 0])
        bfs(i, j, [0, 0, 0, 1], [0, 1, 2, 1])
        bfs(i, j, [0, 1, 1, 2], [0, 0, -1, 0])
        bfs(i, j, [0, 0, -1, 0], [0, 1, 1, 2])

ans.sort(reverse=True)
print(ans[0])