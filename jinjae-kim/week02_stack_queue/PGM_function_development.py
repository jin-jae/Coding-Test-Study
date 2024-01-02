def solution(progresses, speeds):
    to_be_done = []
    answer_idx = []
    answer = []
    
    for pair in zip(progresses, speeds):
        e = (100 - pair[0]) / pair[1]
        to_be_done.append(int(e) if e % 1 == 0 else int(e + 1))
    print(to_be_done)
    
    check_max = 0
    for i, task in enumerate(to_be_done):
        if task > check_max:
            answer_idx.append(i)
            check_max = task
    answer_idx.append(len(to_be_done))
            
    for i in range(len(answer_idx) - 1):
        answer.append(answer_idx[i + 1] - answer_idx[i])

    return answer