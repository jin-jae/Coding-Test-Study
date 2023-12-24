def solution(genres, plays):
    genre_play_count = {}  
    song_list_by_genre = {}  

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
            song_list_by_genre[genre] = []
        genre_play_count[genre] += play
        song_list_by_genre[genre].append((play, i))

    sorted_genres = sorted(genre_play_count, key=genre_play_count.get, reverse=True)

    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(song_list_by_genre[genre], key=lambda x: (-x[0], x[1]))
        answer.extend(idx for _, idx in sorted_songs[:2])
    return answer
