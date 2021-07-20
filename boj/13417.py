# 카드 문자열

T = int(input())

for i in range(T):
    N = int(input())
    cards = list(input().split())
    result = [cards[0]]

    for i in range(1, N):
        if ord(cards[i]) > ord(result[0]):
            result.append(cards[i])
        else:
            result.insert(0, cards[i])
    
    print(''.join(result))
