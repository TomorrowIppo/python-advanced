import sys

def draw_stars(n):
    # Base Case: n이 1이면 별 하나만 담긴 리스트 반환
    if n == 1:
        return ["*"]

    # 재귀적으로 n/3 크기의 별 패턴을 가져옴
    stars = draw_stars(n // 3)
    res = []

    # 1. 상단 (3줄 중 첫 번째 줄 덩어리)
    for s in stars:
        res.append(s * 3)
    
    # 2. 중단 (3줄 중 가운데 줄 덩어리 - 가운데가 비어있음)
    for s in stars:
        res.append(s + " " * (n // 3) + s)
    
    # 3. 하단 (3줄 중 마지막 줄 덩어리 - 상단과 동일)
    for s in stars:
        res.append(s * 3)

    return res

N = int(sys.stdin.readline())
# 리스트에 담긴 문자열들을 줄바꿈으로 합쳐서 한 번에 출력
print('\n'.join(draw_stars(N)))