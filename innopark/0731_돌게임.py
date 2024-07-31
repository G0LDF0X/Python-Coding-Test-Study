#돌은 1개 또는 3개 가져간다.
#상근 찬영순으로 가져간다.
#2의 배수라면 찬영이가 이김
# N = 1 > 상근
# N = 2 > 찬영
# N = 3 > 상근
# N = 4 > 찬영
# N = 5 > 상근
# N = 6 > 찬영
import sys
n = int(sys.stdin.readline().strip())

if n % 2 == 0:
    print('CY')
else:
    print('SK')
