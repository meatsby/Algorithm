import sys

S = sys.stdin.readline().rstrip()
S = ''.join([i for i in S if 65 <= ord(i) <= 90])
check = ['U', 'C', 'P', 'C']
c = True

for i in check:
    if i in S:
        c = True
        S = S[S.index(i) + 1:]
    else:
        c = False
        break

if c == True:
    print('I love UCPC')
else:
    print('I hate UCPC')
