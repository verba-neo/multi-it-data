# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    numbers = [0 for _ in range(200)]
    answer = 0

    for start, end in lines:
        start, end = start + 100, end + 100

        for i in range(start, end):
            numbers[i] += 1

    for num in numbers:
        if num > 1:
            answer += 1

    return answer


# 2
print(solution([[0, 1], [2, 5], [3, 9]]))
# 0
print(solution([[-1, 1], [1, 3], [3, 9]]))
# 8
print(solution([[0, 5], [3, 9], [1, 10]]))
