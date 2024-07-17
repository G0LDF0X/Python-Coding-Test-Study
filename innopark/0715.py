#프로그래머스 베스트앨범

def solution(genres, plays):
    answer = []
    #장르별 총 재생횟수를 담은 딕셔너리
    genre_total = {}
    for i in range(len(genres)):
        if genres[i] in genre_total:
            genre_total[genres[i]] += plays[i]
        else:
            genre_total[genres[i]] = plays[i]
    
    #장르별 노래정보를 고유번호, 재생횟수 고려한 딕셔너리
    genre_songs = {}
    for i in range(len(genres)):
        if genres[i] in genre_songs:
            genre_songs[genres[i]].append((plays[i], i))
        else:
            genre_songs[genres[i]] = [(plays[i], i)]
    
    
    # 3. 장르별 총 재생횟수를 기준으로 내림차순 정렬
    genre_total = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    # 4. 각 장르별로 재생횟수와 고유번호를 기준으로 내림차순 정렬
    for genre in genre_songs:
        genre_songs[genre] = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
    
    # 5. 각 장르별로 최대 2곡씩 선별하여 결과 리스트에 추가
    answer = []
    for genre, _ in genre_total:
        answer.extend([song[1] for song in genre_songs[genre][:2]])
    
    return answer
        
        