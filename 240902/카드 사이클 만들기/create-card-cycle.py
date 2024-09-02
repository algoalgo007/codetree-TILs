n = int(input())
arr1 = []
for _ in range(n):
    arr1.append(input())
arr2 = []
for _ in range(n):
    arr2.append(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

cnt = 0
for i in range(n):
    for j in range(n):
        if arr1[i] == arr2[j] and i != j:
            union_parent(parent, (i + 1), (j + 1))

ans = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    ans[parent[i]].append(1)
print(len(list(set(parent[1:-1]))), end=" ")
print(len(max(ans)))