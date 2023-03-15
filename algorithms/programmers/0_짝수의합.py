# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer


# 30
print(solution(10))

# 6
print(solution(4))
