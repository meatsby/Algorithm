import sys

while True:
    try:
        a, b, c = map(int, sys.stdin.readline().split())
        print(max(c-b, b-a) - 1)
    except:
        break
