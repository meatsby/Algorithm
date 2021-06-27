import sys
case = 1
while True:
    L, P, V = map(int, sys.stdin.readline().rstrip().split())
    if V == 0:
        break
    print('Case %d: %d' %(case, V//P*L + (L if L < V%P else V%P)))
    case += 1
