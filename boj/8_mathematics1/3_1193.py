x = int(input())
n = 0
c = 1 # 지그재그층

while n < x:
    n += c
    c += 1

oe = (c-1)%2 # 지그재그층 홀짝구분
i = n - x # 지그재그 좌표
son = 1 + (1*i) # 분자
mother = (c-1) - (1*i) # 분모

# print(oe)
# print(i)
# print(son)
# print(mother)

if oe == 0:
    print('%d/%d' %(mother, son))
elif oe == 1:
    print('%d/%d' %(son, mother))
