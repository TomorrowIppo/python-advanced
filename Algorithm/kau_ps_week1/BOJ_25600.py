import sys

input = sys.stdin.readline

max_val = 0

for _ in range(int(input())):
    a, d, g = map(int, input().split())
    if a == d + g:
        val = a * (d + g) * 2
    else:
        val = a * (d + g)
    max_val = max(val, max_val)

print(max_val)