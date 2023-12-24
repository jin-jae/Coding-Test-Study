def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part  # 각 참가자 이름에 대해 hash 값을 구한 뒤, dic에 저장
        temp += int(hash(part))  # temp에 hash 값을 더해줌
        
    for com in completion:
        temp -= hash(com)  # 완주한 사람의 hash 값을 빼줌
        
    answer = dic[temp]
    return answer
