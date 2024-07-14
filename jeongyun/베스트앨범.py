def solution(genres, plays):
    answer = []
    songs = {}      # 각 노래의 장르:재생횟수 딕셔너리
    best_genres = {}    # 각 장르의 총 재생횟수 딕셔너리
    n = len(genres)
    
    # 각 노래의 장르별 재생횟수를 저장하는 장르 : (고유번호, 재생횟수) 딕셔너리 
    # 각 장르의 전체 재생횟수를 저장하는 장르: 전체 재상횟수 딕셔너리 
    for i in range(n):
        if genres[i] in songs.keys():
            songs[genres[i]]+=[(i, plays[i])]
            best_genres[genres[i]] += plays[i]
        else:
            songs[genres[i]] = [(i, plays[i])]
            best_genres[genres[i]] = plays[i]

    # 장르별 전체 재생횟수를 내림차순으로 정렬
    sorted_best_genres = dict(sorted(best_genres.items(), key = lambda item: item[1], reverse = True))
    
    # 각 장르의 노래들을 재생횟수 기준 내림차순, 고유번호 기준 오름차순 정렬 
    for key in songs.keys():
        songs[key].sort(key = lambda x: (-x[1], x[0]))
    
    # 장르별 최대 2개까지 answer 에 고유번호를 저장
    for key in sorted_best_genres.keys():
        num = 0
        for item in songs[key]:
            if num >= 2:
                break
            else:
                answer.append(item[0])
                num +=1

    return answer