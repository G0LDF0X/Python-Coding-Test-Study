# list = [0,0,0,1] -> idx = 1, list[idx] = 0 -> idx+1 -> list[idx]= 0 -> idx +1 -> list[idx] = 1
# if list[idx] == 1 -> print(idx)
# if list[idx] == 0 -> idx + 1
# if idx > len(list-1) -> print(-1)

def solution(arr, idx):
    answer = 0

    while True:
        if idx > len(arr)-1:
            return -1
        
        if arr[idx] == 1:
            return idx
        elif arr[idx] == 0:
            idx += 1
        else:
            return -1    

    return answer

# arr = [0,0,0,1]
# idx = 1

# print(solution(arr, idx))

arr = [1, 0, 0, 1, 0, 0]
idx = 4

print(solution(arr, idx))

arr = [1, 1, 1, 1, 0]
idx = 3

print(solution(arr, idx))