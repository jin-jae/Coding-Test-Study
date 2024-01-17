def chk_index(num, array):
    ret = 0
    for a in array:
        if a >= num:
            ret += 1
    return ret

def solution(citations):
    citations.sort()
    answer = [0]
    for i in range(1, len(citations) + 1):
        if (chk_index(i, citations) >= i):
            answer.append(i)
    print(answer)
    return answer[-1]