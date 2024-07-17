def solution(genres, plays):
    album_dict=dict()
    genres_total_dict=dict()
    # return genres_dict
    for g in genres:
        if g in genres_dict:
            genres_dict[g].append( plays[genres.index(g)])
        # else: 
            # genres_dict[g]= plays[genres.index(g)]
    for g in genres:
        if g in genres_total_dict:
            genres_dict[g]+= plays[genres.index(g)]
        else: 
            genres_dict[g]= plays[genres.index(g)]
    genres_total_dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    genres_dict(sorted(d.itmes(), key=lambda x:x[1], reverse=True))
    for key in genres_total_dict.key():
        while True:

            answer.append(plays.index())
            if 
    ???????????????????????????????????

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))