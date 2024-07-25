# 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.

# 막대 1개에 N개가 꽂혀있는 탕후루를 만들었다.
# 최대 9종류의 과일로 만든 탕후루다.
# 가장 바깥 쪽에 있는 것들만 빼서 갯수를 조정 할 수 있다.
# 한 꼬치에 2개만 들어가게한다면 2종류 이하가 확정된다. 완전탐색시 2개 이상의 붙어있는 경우만 탐색한다.


# 예시 1번

5 # 5개 꽂혀 있는 탕후루 만듦.
5 1 1 2 1

4



# ex) -----------포도--귤--귤--딸기--귤-----------


# 두 개  51 / 11 / 12 / 21
# 세 개  511 / 112 / 121
# 네 개  5112(x) / 1121(제일 많음)
# 다섯 개 51121(x)

# 정답 4개(1121)



# 예제 3번

9
1 2 3 4 5 6 7 8 9

# 두 개  12 / 23 / 34 / 45 / 56 / 67 / 78 / 89
# 세 개  123 / 234 / 345 / 456 / 567 / 678 / 789 전부 X
# 네 개  1234 / 2345 / 3456 / 4567 / 5678 / 6789 전부 X
# 다섯 개 12345 / 23456 / 34567 / 45678 / 56789 전부 X
# 여섯 개 123456 / 234567 / 345678 / 456789 전부 X
# 일곱 개 1234567 / 2345678 / 3456789 전부 X
# 여덟 개 12345678 / 23456789 전부 X
# 아홉 개 123456789 전부 X

# 정답 2개(12 / 23 / 34 / 45 / 56 / 67 / 78 / 89)


# 투 포인터 활용하면 쉽게 풀리는걸 인지했지만 내가 투 포인터에 대한 이해가 없으니 사고가 갇힌 느낌이다.
# 초급자 단계에는 이것저것 다 시도하면서 사고를 확장하고 알고리즘의 필요성을 느끼는게 중요한 것 같다.
# 그래서 완전탐색을 하라고 말씀하신 것 같다.