n = int(input())
dict = {}

for i in range(n):
    str = input()
    if str[0] == "a":
        a, b, c = str.split()
        dict[b] = c
    elif str[0] == "f":
        a, b = str.split()
        if b not in dict:
            print("None")
        else:
            print(dict[b])
    else:
        a, b = str.split()
        del dict[b]