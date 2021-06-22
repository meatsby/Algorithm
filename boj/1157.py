a = [0 for i in range(26)]
s = input().lower()
l = []

for i in s:
    a[ord(i)-97] += 1

for i in a:
    if i == max(a):
        l.append(i)

if len(l) != 1:
    print('?')
else:
    print(chr(a.index(max(a))+97).upper())
