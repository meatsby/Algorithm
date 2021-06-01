word = input()
time = 0

for i in word:
    if ord(i) >= 87:
        time += 10
    elif ord(i) >= 84:
        time += 9
    elif ord(i) >= 80:
        time += 8
    elif ord(i) >= 77:
        time += 7
    elif ord(i) >= 74:
        time += 6
    elif ord(i) >= 71:
        time += 5
    elif ord(i) >= 68:
        time += 4
    elif ord(i) >= 65:
        time += 3

print(time)
