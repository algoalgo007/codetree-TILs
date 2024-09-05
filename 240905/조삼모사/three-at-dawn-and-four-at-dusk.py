from itertools import combinations 

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
arr = []
for i in range(n):
    arr.append(i)

def calc(array):
    a = 0
    b = 0
    counter = []
    for i in range(n):
        if i not in array:
            counter.append(i)
        
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            a += graph[array[i]][array[j]]
            a += graph[array[j]][array[i]]
    
    for i in range(len(counter)):
        for j in range(i + 1, len(counter)):
            b += graph[counter[i]][counter[j]]
            b += graph[counter[j]][counter[i]]
    return abs(a - b)

ans = int(1e9)

for c in combinations(arr, n // 2):
    array = list(c)
    result = calc(array)
    ans = min(ans, result)

print(ans)