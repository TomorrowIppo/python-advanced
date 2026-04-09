import sys

# strip()을 써서 개행 문자를 날리고 문자열 그대로 사용
s = sys.stdin.readline().strip()

# 슬라이싱은 문자열에서도 바로 작동하며, 리스트 변환보다 빠릅니다.
if s == s[::-1]:
    print(1)
else:
    print(0)