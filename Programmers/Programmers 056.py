# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):

    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        bridge.pop(0)

        if len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                bridge.append(0)

        answer += 1

    return answer
