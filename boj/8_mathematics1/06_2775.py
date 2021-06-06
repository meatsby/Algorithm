trial = int(input())

for i in range(trial):
    k = int(input())
    n = int(input())
    k0 = [i for i in range(1, n+1)]

    for i in range(k):
        for i in range(1, n):
            k0[i] += k0[i-1]
    print(k0[-1])
