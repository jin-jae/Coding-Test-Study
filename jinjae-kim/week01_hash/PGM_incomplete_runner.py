def solution(participant, completion):
    participant_hash = {}
    for p in participant:
        if p not in participant_hash:
            participant_hash[p] = 1 
        else:
            participant_hash[p] += 1
    for completed in completion:
        participant_hash[completed] -= 1
    answer = [k for k, v in participant_hash.items() if v == 1]
    return answer[0]
