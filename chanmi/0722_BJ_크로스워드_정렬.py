import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
sort_list = []

# 2중 배열 저장용
word_data = []

# 가로줄 세기 + 데이터 저장(세로줄 용)
for i in range(R):
    sentence = input().strip()
    word_list = list(sentence)
    word_data.append(word_list)

    word_list = sentence.split("#")
    for word in word_list:
        if len(word) > 1:
            sort_list.append(word)

for i in range(C):
    sentence = ""
    for j in range(R):
        sentence += word_data[j][i]
    word_list = sentence.split("#")
    for word in word_list:
        if len(word) > 1:
            sort_list.append(word)

print("이중배열\n", word_data)
print("정렬 전\n", sort_list)

sort_list.sort()
print(sort_list[0])