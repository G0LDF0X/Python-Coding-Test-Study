# 0 ~ 9까지는 순차적으로 출력(1번째 ~ 10번째)
# 10, 11, 12, 13, 14, 15 -> 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5

# 리스트를 만든다.
# t * m은 배열 수 -> 15
# 배열을 str로 변환해서 한자리 수로 변환
# str을 int형으로 변환
# 전체 리스트 출력

# p = 1, m = 2, t =4 / 1, 3, 5, 7, 9

# 0, 1, 2 = (1, 0), 3 = (1, 1), 4 = (1, 1, 0) -> 10진수를 2진수로 바꾸는 로직 필요
# 10진수를 16진수로 바꾸는 로직 필요


def solution(n, t, m, p):
    c_list = []
    answer = ''
    if n == 2:
        pass
    elif n == 16:
        pass
    elif n == 10:
        for i in range(15):
            for one_digit in str(i):
                c_list.append(int(one_digit))
    print(c_list)

    return answer


solution(10, 0, 0, 0)