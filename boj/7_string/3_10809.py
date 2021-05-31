a = [-1 for i in range(123)]
s = input()

for i in s:
    if a[ord(i)] == -1:
        a[ord(i)] = s.index(i)


print(*a[97:])
