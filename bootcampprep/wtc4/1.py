def solution(arr):
    answer = []
    l = [0, 0, 0]

    for a in arr:
        if a == 1:
            l[0] += 1
        elif a == 2:
            l[1] += 1
        elif a == 3:
            l[2] += 1

    for i in l:
        answer.append(max(l) - i)

    return answer

print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))
print(solution([1, 2, 3]))
print(solution([1]))
print(solution([2]))
print(solution([3]))