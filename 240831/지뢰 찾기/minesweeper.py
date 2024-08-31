dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
graph = [["."] * n for _ in range(n)]
for i in range(n):
    str = input()
    for j in range(n):
        graph[i][j] = str[j]
check = [["."] * n for _ in range(n)]
for i in range(n):
    str = input()
    for j in range(n):
        check[i][j] = str[j]

def mine(x, y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == "*":
            cnt += 1
    return cnt
for i in range(n):
    for j in range(n):
        if check[i][j] == "x":
            result = mine(i, j)
            check[i][j] = result
for i in range(n):
    for j in range(n):
        print(check[i][j], end="")
    print()