# permutaions 로 가능한 모든 경우를 저장하여 중복을 제거하고 정렬. -> 메모리 낭비, 시간 오래걸림. 
from itertools import permutations

def solution(word):
    answer = 0
    aeiou = ['A', 'A', 'A', 'A', 'A', 'E', 'E','E','E','E','I', 'I','I','I','I','O', 'O','O','O','O','U','U','U','U','U']
    dictionary = []
    
    for i in range(1, 6):
        ps = permutations(aeiou, i)
        for p in ps:
            dictionary.append(''.join(p))
            
    dictionary = list(set(dictionary))
    dictionary.sort()
    # print(dictionary[:20])
    
    answer = dictionary.index(word) +1
    
    return answer


# # product 를 사용하여 효율적으로 작성한 코드 ( by. chatGPT)
# from itertools import product

# def solution(word):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     dictionary = []
    
#     # 길이 1부터 5까지의 모든 가능한 단어 생성
#     for i in range(1, 6):
#         for comb in product(vowels, repeat=i):
#             dictionary.append(''.join(comb))
    
#     # 사전순으로 정렬된 리스트에서 단어의 위치 찾기
#     dictionary.sort()
    
#     # word의 위치는 1-based index
#     answer = dictionary.index(word) + 1
    
#     return answer


