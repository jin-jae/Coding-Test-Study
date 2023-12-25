def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = []
        clothes_dict[cloth[1]].append(cloth[0])
    print(clothes_dict)
    
    answer = 1
    for k, v in clothes_dict.items():
        answer *= len(v) + 1
    return answer - 1