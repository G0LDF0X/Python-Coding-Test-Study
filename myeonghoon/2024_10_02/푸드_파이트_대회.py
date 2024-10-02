# 짝수 0 짝수 
# food에는 배열의 위치에 따라 0:물, 1: 가장 낮은 칼로리, n: 가장 높은 칼로리로 분류한다.
# 각 칼로리에 해당하는 음식을 앞쪽과 뒷쪽에 배치하는데 음식의 갯수가 똑같아야 한다.

# food의 낮은 칼로리부터 높은 칼로리의 음식 순서대로 출력하는 기능
def a():
    for calorie in food:
        number_of_food = food[calorie]
        print(number_of_food)

# n을 2로 나눴을 때 몫을 구하는 기능
def b(number_of_food):
    food_for_one_person = number_of_food // 2

# 칼로리를 1인분의 음식만큼 출력하는 기능
def c(food_for_one_person, calorie):
    for _ in range(food_for_one_person):
            print(calorie)

# string에 추가하는 기능
def d(answer, calorie):
    answer += str(calorie) 

# 정렬된 순서를 뒤집는 기능
def e(answer):
    reversed_answer = answer[::-1]
    return reversed_answer
 
def solution(food):
    answer = ''
    for calorie in range(len(food)):
        number_of_food = food[calorie]
        food_for_one_person = number_of_food // 2
        for _ in range(food_for_one_person):
            answer += str(calorie)
    reversed_answer = answer[::-1]
    answer += '0'        
    answer += reversed_answer        
    return answer 

food = [1, 3, 4, 6]
print(solution(food))

food = [1, 7, 1, 2]
print(solution(food))