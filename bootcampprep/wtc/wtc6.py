# 프로그래밍6
import sys
input = sys.stdin.readline

def solution(totalTicket, logs):
    result = []
    current = []
    nt = 0

    for log in logs:
        uid, cmd, t = log.split()
        t = int(t.split(":")[0])*3600 + int(t.split(":")[1])*60 + int(t.split(":")[2])

        if t > nt and current and totalTicket > 0:  # 다음 들어온 log 의 시간이 nt 보다 크고 현재 접속중인 사람이 있으며 티켓이 남아있을 경우
            result.append(current.pop())  # 티켓팅에 성공한 사람을 result 에 삽입
            totalTicket -= 1  # 티켓 하나 소진
        
        if cmd == "request" and not current:  # "request" 요청을 했고 현재 접속 중인 사람이 없을 경우
            current.append(uid)  # 접속중에 uid 를 삽입
            nt = t + 60  # 접속유지시간 갱신
        
        if cmd == "leave" and current[0] == uid:  # "leave" 요청이고 uid 가 접속 중인 uid 와 같을 경우
            current.pop()  # 티켓팅 실패
    
    if current and nt < 36000 and totalTicket > 0:  # current 에 남아있는 사람이 있고 접속유지시간이 10시 이전이며 티켓이 남아있을 경우
        result.append(current.pop())  # 티켓팅 성공
        totalTicket -= 1  # 티켓 하나 소진

    return sorted(set(result))

print(solution(
    2000, [
        "woni request 09:12:29", 
        "brown request 09:23:11", 
        "brown leave 09:23:44", 
        "jason request 09:33:51", 
        "jun request 09:33:56", 
        "cu request 09:34:02", 
        "woni request 09:35:51"]))
