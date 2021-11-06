def calcT(s):
    if len(s) == 4:
        t = int(s[:2])
        if s[2:] == "PM":
            t += 12
    else:
        t = int(s[:1])
        if s[1:] == "PM":
            t += 12

    return t

def solution(time, plans):
    fri = 18
    mon = 13
    answer = ""

    for plan in plans:
        loc = plan[0]
        start = 8.5 if fri - calcT(plan[1]) > 8.5 else fri - calcT(plan[1])
        end = 5 if calcT(plan[2]) - mon > 5 else calcT(plan[2]) - mon
        needed = start + end
        print(needed)

        if needed <= 0:
            answer = loc
        elif needed > 0:
            if time >= needed:
                time -= needed
                answer = loc

    return answer

print(solution(4, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"], ["뉴욕", "6PM", "1PM"]]))