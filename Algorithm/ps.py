import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
# 1. 리스트 컴프리헨션으로 독립된 객체 생성
tree = [[0, 0] for _ in range(4 * N + 1)]

# 2. data를 0-indexed로 깔끔하게 입력받기
A = list(map(int, input().split()))
data = []
for i in range(N):
    data.append([i + 1, A[i]]) # [인덱스, 값] 저장

# 최솟값 비교 함수: 값이 작으면 선택, 같으면 인덱스 작은 것 선택
def get_min(a, b):
    if a[1] < b[1]: return a
    elif a[1] > b[1]: return b
    else: return a if a[0] < b[0] else b

def build(node, start, end):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = get_min(build(node*2, start, mid), build(node*2 + 1, mid + 1, end))
    return tree[node]

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = [idx + 1, val] # 문제의 출력은 1-based 인덱스
        return tree[node]
    mid = (start + end) // 2
    tree[node] = get_min(update(node*2, start, mid, idx, val), 
                         update(node*2 + 1, mid + 1, end, idx, val))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return [float('inf'), float('inf')]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return get_min(query(node*2, start, mid, left, right),
                   query(node*2 + 1, mid + 1, end, left, right))

build(1, 0, N - 1)

M = int(input())
for _ in range(M):
    order, x, y = map(int, input().split())
    if order == 1:
        # x번째 수를 y로 바꿈 (x는 1-based이므로 0-based로 보정)
        update(1, 0, N - 1, x - 1, y)
    else:
        # x번부터 y번까지 중 최솟값의 인덱스 출력
        print(query(1, 0, N - 1, x - 1, y - 1)[0])