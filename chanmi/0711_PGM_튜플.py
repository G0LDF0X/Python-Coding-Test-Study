def solution(s):
    # 보기 편하게 입력 문자열 s를 리스트로 변환하며, 그 과정에서 불필요한 부분들을 전처리
    tuple_list = s.split("},")
    for i in range(len(tuple_list)):
        tuple_list[i] = tuple_list[i].replace("{", "").replace("}", "").split(",")

    # 길이 순으로 정렬
    tuple_list.sort(key=lambda x: len(x))

    answer = []
    for item in tuple_list:
        for i in item:
            if int(i) not in answer:
                answer.append(int(i))

    return answer

# 가장 짧은 리스트에 들어있는 원소가 리스트의 첫 배열.
# 그 다음 리스트에 들어있는 원소 중 첫 배열에 없는 원소가 리스트의 두 번째 배열.]
# 이런식으로 접근하면 될듯...