n = int(input())
dict = {}
color = set()
for _ in range(n):
    str = input()
    color.add(str)
    if str in dict:
        dict[str] += 1
    else:
        dict[str] = 1

max = -1
color = list(color)
for i in range(len(color)):
    if dict[color[i]] > max:
        max = dict[color[i]]
print(max)