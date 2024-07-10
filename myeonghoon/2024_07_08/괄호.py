# 한 칸 씩 돌 때마다 조회하는 게 기본 작업인 것 같다
# 1 2 3
# ( } x
# (, [, { 는 무조껀 왼쪽에 있어야 한다.
# b 포인트가 f+1 이면 참
# f 포인트가 가리키는 문자가 

left_parentheses = ['(', '{', '['] # 참이 되는 조합은 11, 22, 33
right_parentheses = [')', '}', ']']

# x의 값만큼 배열을 왼쪽으로 회전시키는 함수
def left_lotation(arr):
    # 맨 앞에 있는 0인덱스를 끝으로 위치를 옮겨주면 된다.
    start = 0
    # end = start-1 # null을 먼저 이동시켜야 되나?

    move_par = arr.pop(start)
    arr.append(move_par)
    return arr
