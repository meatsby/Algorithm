import sys

pages = list(map(int, sys.stdin.readline().split()))

if len(pages) != 4 or pages[1] - pages[0] != 1 or pages[3] - pages[2] != 1 or max(pages) > 398 or min(pages) < 3 or pages[0]%2 != 1 or pages[2]%2 != 1 or pages[1]%2 != 0 or pages[1]%2 != 0:
    print(-1)

else:
    pobi = [pages[0], pages[1]]
    crong = [pages[2], pages[3]]
    p_score = []
    c_score = []
    for p in range(0, 2):
        sum = 0
        prod = 1
        for i in str(pobi[p]):    
            sum += int(i)
            prod *= int(i)
        p_score.append(sum)
        p_score.append(prod)
        sum = 0
        prod = 1
        for i in str(crong[p]):    
            sum += int(i)
            prod *= int(i)
        c_score.append(sum)
        c_score.append(prod)
    if max(p_score) > max(c_score):
        print(1)
    elif max(p_score) == max(c_score):
        print(0)
    elif max(p_score) < max(c_score):
        print(2)
