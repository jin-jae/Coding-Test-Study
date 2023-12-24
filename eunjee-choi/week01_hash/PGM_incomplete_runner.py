def solution(participant, completion):
    answer = ''
    hash_table = {}

    for name in participant:
        if name in hash_table:
            hash_table[name] += 1
        else:
            hash_table[name] = 1

    for name in completion:
        hash_table[name] -= 1

    for name in participant:
        if hash_table[name] > 0:
            return name
        
    answer = list(hash.keys())[0]
    return answer

