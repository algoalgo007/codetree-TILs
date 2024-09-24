from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

ans = int(1e9)

for c in combinations(arr, 4):
    temp = []
    for x in c:
        temp.append(x)
    val = sum(temp)
    for a in combinations(temp, 2):
        aa = list(a)
        ans = min(ans, abs(abs(val - sum(aa) - sum(aa))))
print(ans)