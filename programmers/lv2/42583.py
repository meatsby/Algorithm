# Lv2 다리를 지나는 트럭
# deque 가 더 시간이 빠른거로 알고 있는데 왜 deque 를 쓰면 시간초과가 뜨나요?

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
                
    return answer
