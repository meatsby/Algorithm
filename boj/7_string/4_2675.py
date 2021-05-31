t = int(input())
new = ''

for i in range(t):
    r, s = input().split()
    for i in s:
        new += i*int(r)
    print(new)
    new = ''
