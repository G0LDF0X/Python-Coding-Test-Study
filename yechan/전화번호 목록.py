import sys
sys.stdin.readline()

def solution(phone_numbers):
    phone_numbers.sort()

        # 정렬된 목록에서 각 전화번호가 다음 전화번호의 접두사가 되는지 확인
    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"


