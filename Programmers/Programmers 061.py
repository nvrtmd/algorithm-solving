# 베스트앨범
def solution(genres, plays):
    answer = []
    songs_dict = {genre: [] for genre in list(set(genres))}
    genres_dict = {genre: 0 for genre in list(set(genres))}

    for idx, song in enumerate(zip(genres, plays)):
        songs_dict[song[0]].append((song[1], idx))
        genres_dict[song[0]] += song[1]

    sorted_genres_arr = sorted(
        genres_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres_arr:
        sorted_songs_dict = sorted(
            songs_dict[genre], key=lambda x: (x[0], -x[1]), reverse=True)
        if len(sorted_songs_dict) < 2:
            answer.append(sorted_songs_dict[0][1])
        else:
            for i in range(2):
                answer.append(sorted_songs_dict[i][1])

    return answer
