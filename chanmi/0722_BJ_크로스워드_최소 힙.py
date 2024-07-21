import sys
import heapq

# heapq로 풀기
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
heap = []

# 2중 배열 저장용
word_data = []
# 가로줄 세기 + 데이터 저장(세로줄 용)
for i in range(R):
    sentence = input().strip()
    word_list = list(sentence)
    word_data.append(word_list)

    sentence = sentence.replace("#", " ")
    word_list = sentence.split(" ")
    for word in word_list:
        if len(word) > 1:
            heapq.heappush(heap, word)

print(word_data)

for i in range(C):
    sentence = ""
    for j in range(R):
        print("i, j", i, j)
        sentence += word_data[j][i]
    sentence = sentence.replace("#", " ")
    word_list = sentence.split(" ")
    for word in word_list:
        if len(word) > 1:
            heapq.heappush(heap, word)
    
print(heap[0])