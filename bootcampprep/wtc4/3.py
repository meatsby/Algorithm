def solution(ings, menu, sell):
    ingD = {}
    for ing in ings:
        ingN = ing.split()[0]
        ingP = int(ing.split()[1])
        ingD[ingN] = ingP

    menuR = {}
    for m in menu:
        menuN = m.split()[0]
        ingL = m.split()[1]
        menuP = int(m.split()[2])

        for i in ingL:
            menuP -= ingD[i]

        menuR[menuN] = int(menuP)

    answer = 0
    for s in sell:
        sellN = s.split()[0]
        sellC = int(s.split()[1])
        answer += menuR[sellN] * sellC

    return answer

print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))