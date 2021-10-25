# Lv2 오픈채팅방

def solution(record):
    answer = []
    idmap = {}

    for l in record:
        log = l.split()
        cmd = log[0]
        if cmd == "Enter" or cmd == "Change":
            id = log[1]
            name = log[2]
            idmap[id] = name

    for l in record:
        log = l.split()
        cmd = log[0]
        id = log[1]
        if cmd == "Enter":
            answer.append(f"{idmap[id]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{idmap[id]}님이 나갔습니다.")

    return answer