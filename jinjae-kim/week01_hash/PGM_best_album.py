def solution(genres, plays):
    songs = {}
    answer = []
    
    for i, g in enumerate(genres):
        if g not in songs:
            songs[g] = []
        songs[g].append([plays[i], i])
    
    srt = dict(sorted(songs.items(), key=lambda x: sum(-v[0] for v in x[1])))
    
    for k, v in srt.items():
        if len(v) == 1:
            answer.append(v[0][1])
        elif len(v) >= 2:
            srt[k] = sorted(v, key=lambda x: -x[0])
            print(srt[k])
            answer.append(srt[k][0][1])
            answer.append(srt[k][1][1])
        
    return answer