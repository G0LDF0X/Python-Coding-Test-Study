def solution(cards1, cards2, goal):
    answer = ''
    i = 0
    j = 0

    for goal_word in goal:
        if i < len(cards1) and goal_word == cards1[i]:
            i += 1
        elif j < len(cards2) and goal_word == cards2[j]:
            j += 1            
        
    if i == len(cards1) and j == len(cards2):
        return "Yes"
    elif i+j == len(goal):
        return "Yes"
    else:
        return "No"   
    

cards1 = ["i", "drink", "water"] # i의 idx < drink의 idx < water idx  
cards2 = ["want", "to"] # want의 idx < to의 idx 
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))

cards1 = ["i", "water", "drink"] # i의 idx < drink의 idx < water idx  
cards2 = ["want", "to"] # want의 idx < to의 idx 
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))

cards1 = ["i", "water", "drink"] # i의 idx < drink의 idx < water idx  
cards2 = ["want", "to"] # want의 idx < to의 idx 
goal = ["i", "want", "to", "water"]

print(solution(cards1, cards2, goal))

# cards1에서 i, cards2에서 want, to, cards1에서 drink, water = i want to drink, water
# goal에 있는 단어 배열을 완성시켜야 한다.
# goal이 i일때, cards1에서 i를 찾고, 
# want일 때 cards1에서 찾아보고 없으면 cards2에서 찾는다?
# 시간이 오래 걸릴 것 같음. 벌써 cards1을 순회하고, cards2를 순회하고 있음.

# cards1과 goal의 요소들이 같은 순서로 나타나는지 확인하려면, 
# goal 리스트를 순회하면서 cards1의 요소들이 같은 순서로 나타나는지 
# 확인하면 됩니다. 이를 위해 두 개의 포인터를 사용할 수 있습니다: 하나는 goal 
# 리스트를 순회하고, 다른 하나는 cards1 리스트를 순회합니다.

# goal을 순회하면 i, want, to, drink, water
# 그와 동시에 cards1을 순회하면 i, drink, water
# goal에서 i일 때 cards1 i -> true
# goal, want일 때 cards1 drink -> false
# goal, to일 때 cards1 drink -> false
# goal, drink일 때 cards1 drink -> true
# 만약
# goal, water일 때 cards1 drink -> false
# goal, drink일 때 cards1 drink -> true
# cards 길이 = 3, i = 2 이므로 순서가 다르다.