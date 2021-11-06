def solution(log):
    ans = 0

    for i in range(0, len(log), 2):
        start = list(map(int, log[i].split(":")))
        startT = start[0]*60 + start[1]

        end = list(map(int, log[i+1].split(":")))
        endT = end[0]*60 + end[1]

        studyT = endT - startT

        if 5 <= studyT <= 105:
            ans += studyT
        
        if studyT > 105:
            ans += 105

    h = str(ans//60).zfill(2)
    m = str(ans%60).zfill(2)

    answer = h + ":" + m

    return answer

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))
print(solution(["01:00", "01:04", "01:05", "01:10", "15:00", "16:45", "17:00", "18:46"]))