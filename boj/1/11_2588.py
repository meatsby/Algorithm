a = int(input())
b = input()
list = list(b)
list.reverse()

for i in list:
    print(a * int(i))

print(a * int(b))
