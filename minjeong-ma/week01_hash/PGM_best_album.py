def solution(genres, plays):
    answer = []
    dic = {}

    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for i in dic:
        temp = []
        for j in range(len(genres)):
            if i[0] == genres[j]:
                temp.append([j, plays[j]])
        temp = sorted(temp, key=lambda x: x[1], reverse=True)

        answer.append(temp[0][0])
        if len(temp) > 1:
            answer.append(temp[1][0])
    return answer
