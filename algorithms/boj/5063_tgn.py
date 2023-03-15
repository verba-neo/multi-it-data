T = int(input())

for _ in range(T):
    # r => 광고 하지 않았을 때
    # e => 광고 했을 때
    # c => 광고 비용
    # e - c => 광고를 하고 얻는 수익
    r, e, c = map(int, input().split())

    if e - c > r:
        print('advertise')
    elif e - c == r:
        print('does not matter')
    else:
        print('do not advertise')
