def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    cur_weight = 0
    while truck_weights:
        time += 1
        cur_weight -= bridge.pop(0)
        if cur_weight + truck_weights[0] <= weight:
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else: 
            bridge.append(0)

    time += bridge_length
    return(time)