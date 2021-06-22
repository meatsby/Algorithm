A = int(input())
B = int(input())
C = int(input())
ABC = A * B * C
count = [0 for i in range(10)]

for i in str(ABC):
    count[int(i)] += 1

for i in range(10):
    print(count[i])
