# 그리 크기 증가시키기
# k만큰 ., x를 배로 증가시켜야함.
# .xx 라면 -> . 2배, x 2배, x 2배 차례대로 2배시키면 된다.
# 문자열을 2배시킨다는 의미? -> 반복문을 더 돌리면 된다.

# ., x, x, 를 각각 출력.
# k의 배만큼 for문 반복
# 리스트에 담기
# picture[0~ 6]

 
def solution(picture, k):
    answer = []    
    
    for z in range(len(picture)):        
        for i in picture[z]:
            print(i)
            string = ""
            for _ in range(k):
                string += i
            answer.append(string)
    
    return answer


picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2

print(solution(picture, k))

# for i in solution(picture, k):
#     print(i)