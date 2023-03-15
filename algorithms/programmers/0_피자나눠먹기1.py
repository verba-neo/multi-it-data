# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    return n // 7 + 1 if n % 7 else n // 7


# 1
print(solution(7))
# 1
print(solution(1))
# 3
print(solution(15))
