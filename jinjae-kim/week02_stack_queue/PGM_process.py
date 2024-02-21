def has_larger_element(needle, haystack):
    for e in haystack:
        if needle < e:
            return True
    return False

def solution(priorities, location):
    answer = 1
    process = []
    for i, e in enumerate(priorities):
        process.append([i, e])
    while process:
        tmp = process.pop(0)
        if has_larger_element(tmp[1], [a[1] for a in process]):
            process.append(tmp)
        else:
            if location == tmp[0]:
                return answer
            else:
                answer += 1
    print(process)
    return answer