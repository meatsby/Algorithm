a = [0 for i in range(26)]
s = input().lower()
l = []

for i in s:
    a[ord(i)-97] += 1

for i in a:
    if i != 0:
        l.append(i)

if len(l) != len(set(l)):
    print('?')
else:
    print(chr(a.index(max(a))+97).upper())
