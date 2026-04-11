import sys
from collections import deque

input = sys.stdin.readline


# 전처리
M, N = map(int, input().split())

board = [input().strip() for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
vis = [[False for _ in range(N)] for _ in range(M)]

#print(board)


# BFS
def BFS(x, y):
    global board, dx, dy

    vis[x][y] = True

    q = deque()
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        for dir in range(4):
            nx, ny = (cur_x + dx[dir], cur_y + dy[dir])

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if vis[nx][ny] or board[nx][ny] != '0':
                continue

            vis[nx][ny] = True
            q.append((nx, ny))


# Flood-Fill
for i in range(N):
    if board[0][i] == '0':
        BFS(0, i)

for i in range(N):
    if vis[M - 1][i]:
        print("YES")
        exit()

print("NO")
        

