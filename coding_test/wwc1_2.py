import sys

word = sys.stdin.readline()

for i in word:
    if 122 >= ord(i) >= 97:
        print(chr(219 - ord(i)), end='')
    elif 90 >= ord(i) >= 65:
        print(chr(155 - ord(i)), end='')
    else:
        print(i, end='')
