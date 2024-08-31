n, m = map(int, input().split())
arr = list(map(int, input().split()))
dict = {}
for i in range(n):
    if arr[i] not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] += 1

check = list(map(int, input().split()))
for i in range(m):
    if check[i] in dict:
        print(dict[check[i]], end=" ")
    else:
        print(0, end=" ")