def solution(arr):
    past = arr[0]
    answer = [past]
    for i in range(1, len(arr)):
        if arr[i] != past:
            answer.append(arr[i])
            past = arr[i]
    return answer