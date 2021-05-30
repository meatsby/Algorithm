n = int(input())
nl = []
count = 0

for i in range(n):
    l = list(map(int, input().split()))
    for i in range(l[0]):
        nl.append(l[i+1])
      # print(nl)
      # print(sum(nl)/l[0])
    for i in nl:
        if i > sum(nl)/l[0]:
            count += 1
      # print(count)
    print('%.3f' %(count/l[0]*100) + '%')
    nl = []
    count = 0
