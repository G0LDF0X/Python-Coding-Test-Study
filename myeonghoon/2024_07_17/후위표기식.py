# 중위 표기식을 후위 표기식으로 바꿔라
# a+b*c -> (a+(b*c)) = abc*+
# ((A+(B*C))-(D/E)) ->abc*+ de/-

def test_1(n):
    pass 

# 배열로 바꿀까?
# 우선 순위 
# * /는 앞에서부터 순서대로
# * / 는 +, - 보다 우선순위가 높기 때문에 먼저? 배열에서 빠져나와야 한다.
# 굳이 먼저 빠져나올 필요가 있나?
# 