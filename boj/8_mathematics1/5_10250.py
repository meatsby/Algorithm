trial = int(input())

for i in range(trial):
    h, w, n = map(int, input().split())  # h:높이,w:너비,n:번째
    room = n//h+1
    floor = n%h*100
    if n%h == 0:
        room = n//h
        floor = h*100
    print(floor + room)
