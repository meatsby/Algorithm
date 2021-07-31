# Lv1 크레인 인형뽑기 게임

def solution(board, moves):
    result = [0]
    answer = 0
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if result[-1] != board[j][moves[i]-1]:
                    result.append(board[j][moves[i]-1])
                else:
                    del result[-1]
                    answer += 2
                board[j][moves[i]-1] = 0
                break
    
    return answer