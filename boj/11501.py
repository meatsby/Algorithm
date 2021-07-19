# 주식
# 정답 참고
# 리스트를 어떤 부분까지 슬라이싱해서 푸는 것 보다 뒤에서부터 푸는게 훨씬 효과적

T = int(input())

for i in range(T):
    N = int(input())
    stock_price = list(map(int, input().split()))
    stock_price.reverse()
    max_p = 0
    profit = 0

    for i in stock_price:
        if i >= max_p:
            max_p = i
        else:
            profit += max_p - i

    print(profit)
