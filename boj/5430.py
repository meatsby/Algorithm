# AC
# 시간 초과
# 정답 참고

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    p.replace('RR', '')
    n = int(input())
    x = input().rstrip()[1:-1].split(',')
    l, r, b = 0, 0, True

    for c in p:
        if c == 'R':
            b = not b
        elif c == 'D':
            if b:
                l += 1
            else:
                r += 1
    
    if l+r > n:
        print('error')
    else:
        x = x[l:n-r]
        if b:
            x = ','.join(x)
        else:
            x = ','.join(x[::-1])
        print(f'[{x}]')
