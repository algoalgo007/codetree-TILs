n, m = map(int, input().split())
dict1 = {}
dict2 = {}

idx = 1
for i in range(n):
    str = input()
    dict1[str] = idx
    dict2[idx] = str
    idx += 1
for i in range(m):
    str = input()
    if str not in dict1:
        print(dict2[int(str)])
    else:
        print(dict1[str])