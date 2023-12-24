def solution(clothes):
    dic = {} 
    for name, category in clothes:
        if category in dic.keys():
            dic[category] += [name]
        else:
            dic[category] = [name]
    
    answer = 1
    for key, value in dic.items():
        answer *= (len(value) + 1)
        
    return answer -1
