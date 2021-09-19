# 숫자 야구게임

ans = "713"

while True:
    guess = input("숫자를 입력해주세요 ex)123 : ")
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] in ans and guess[i] == ans[i]:
            strike += 1
        elif guess[i] in ans:
            ball += 1
    if guess == ans:
        print("3 스트라이크")
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        break
    elif strike > 0 and ball > 0 :
        print(f"{strike} 스트라이크 {ball}볼")
    elif strike > 0:
        print(f"{strike} 스트라이크")
    elif ball > 0:
        print(f"{ball}볼")
    else:
        print("낫싱")
