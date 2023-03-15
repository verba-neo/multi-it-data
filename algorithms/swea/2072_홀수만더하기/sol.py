# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq
import sys
sys.stdin = open('input.txt')

# Test Case 개수
T = int(input())

for tc in range(1, T+1):
    total = 0
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num % 2:
            total += num

    print(f'#{tc} {total}')


