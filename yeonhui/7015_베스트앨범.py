def solution(genres, plays):
    answer = []

    # 장르별 묶음 딕셔너리 
    # { 장르1: [[노래1 재생 횟수 :노래1 고유 번호],[노래2 재생 횟수: 노래2 고유번호]...]}
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i]) # 있는 장르면 재생수, 고유 번호 추가
        else : 
            dic[genres[i]] = [[plays[i],i]]

    #장르별 총 재생수
    genre_rank ={}
    for genre in dic.keys():
        songs = dic[genre]
        total_play = 0
        for song in songs:
            total_play+=song[0]
        genre_rank[genre] = total_play

    # 1번 조건 : 속한 노래가 많이 재생된 장르를 먼저 수록   
    # genre_rank를 재생 횟수가 큰 순으로 정렬 
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    
    # 2번 조건 :장르 내에서 많이 재생된 노래를 먼저 수록
    # genre_rank에 저장되어 있는 장르 순으로 dic에서 해당 장르를 key로 가진 value를 확인
    for genre in genre_rank:
        # 3번 조건 : 장르 내에서 많이 재생된 노래를 먼저 수록
        #2차원 배열인 value를 다중 조건으로 정렬 (첫번째 인자인 곡 재생 수를 기준으로 내림차순 정렬 후,두번째 인자인 곡 고유 번호를 기준으로 오름차순 정렬)
        song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
        best_two = 0
        # 정렬된 배열을 하니씩 확인하면서 answer에 고유 번호를 순서대로 저장 , 만약 한 장르의 곡이 두 곡 저장되면 해당 장르에서 반복 중지
        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break

    return answer