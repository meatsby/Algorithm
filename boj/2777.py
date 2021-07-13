T = int(input())

for i in range(T):
    N = int(input())
    l = []
    i = 9
    if N < 10:
        print(1)
    else:
        while True:
            if i == 1:
                break
            elif N%i == 0:
                N //= i
                l.append(i)
            else:
              i -= 1
        if N != 1:
            print(-1)
        else:
            print(len(l))
