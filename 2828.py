import sys

screen, basket = map(int, sys.stdin.readline().rstrip().split())
n_apl = int(sys.stdin.readline().rstrip())

start = 1
end = basket
result = 0

for i in range(n_apl):
    pos = int(sys.stdin.readline().rstrip())
    if pos > end:
        result += pos - end
        end = pos
        start = pos - basket + 1
    elif start > pos:
        result += start - pos
        start = pos
        end = pos + basket - 1

print(result)
