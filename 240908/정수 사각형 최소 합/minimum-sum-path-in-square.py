n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for j in range(n-2, -1, -1):
    graph[0][j] += graph[0][j+1]
for i in range(1, n):
    graph[i][n-1] += graph[i-1][n-1]

for i in range(1, n):
    for j in range(n-2, -1, -1):
        graph[i][j] += min(graph[i-1][j], graph[i][j+1])

print(graph[n-1][0])