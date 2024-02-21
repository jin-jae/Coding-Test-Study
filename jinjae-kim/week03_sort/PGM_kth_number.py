def solution(array, commands):
    answer = []
    for command in commands:
        tmp = array[command[0] - 1:command[1]]
        tmp.sort()
        answer.append(tmp[command[2] - 1])
    return answer