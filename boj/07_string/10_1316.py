n = int(input())

for i in range(n):
    s = input()
    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i] in s[i+1:]:
            n -= 1
            break

print(n)
