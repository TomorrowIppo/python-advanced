# boj-9251

import sys

# input을 정의할 때 strip()을 포함하거나, 읽을 때 붙여주세요.
input = sys.stdin.readline

# 1. .strip()으로 양 끝 공백/줄바꿈 제거
s1 = input().strip()
s2 = input().strip()

n1 = len(s1)
n2 = len(s2)

# 2. DP 테이블 초기화
lcs = [[0] * (n2 + 1) for _ in range(n1 + 1)]

# 3. LCS 알고리즘 수행
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

# 4. 결과 출력 (가장 마지막 칸이 최댓값임이 보장됨)
print(lcs[n1][n2])

for ls1 in lcs:
    for ls2 in ls1:
        print(ls2, end=' ')
    print()