A, B = map(int, input().split())
N = int(input())
fav = [int(input()) for i in range(N)]
mov = [(abs(fav[i]-B) + 1) for i in range(N)]

print(min(abs(A-B), min(mov)))
