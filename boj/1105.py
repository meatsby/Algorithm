# 팔
# 시간초과, 정답참고
# 두 숫자의 길이가 다를 경우 8이 나올 경우 0
# 같을 경우 맨 앞자리부터 서로가 같고 8인지 확인 후 cnt +=1 씩

L, R = map(str, input().split())
cnt = 0

if len(L) != len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break

print(cnt)
