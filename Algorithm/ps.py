import sys

input = sys.stdin.readline

inp = list(input().strip())
stack = []

for c in inp:
    if c == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)
    
cnt = 0
while stack:
    stack.pop()
    cnt += 1
print(cnt)
