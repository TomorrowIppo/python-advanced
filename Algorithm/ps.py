import sys, heapq


# Week9 | Prioirty-Queue
def solve_boj_9662():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        K = int(input())
        
        max_pq = []
        min_pq = []
        
        # 실제 삽입된 데이터의 개수만큼만 마킹하기 위한 배열
        is_deleted = [False] * K
        data_id = 0 # 삽입되는 데이터의 진짜 고유 ID (0부터 시작)

        for _ in range(K):
            command, num_str = input().split()
            num = int(num_str)

            if command == 'I':
                # 삽입할 때 현재 데이터의 고유 ID(data_id)를 매칭해서 넣음
                heapq.heappush(max_pq, (-num, data_id))
                heapq.heappush(min_pq, (num, data_id))
                data_id += 1 # 다음 데이터를 위해 고유 ID 1 증가

            else:   # command == 'D'
                if num == 1:    # 최댓값 삭제
                    # 힙의 탑에 있는 원소의 ID가 이미 삭제된 것이라면 청소
                    while max_pq and is_deleted[max_pq[0][1]]:
                        heapq.heappop(max_pq)
                    if max_pq:
                        # 진짜 살아있는 최댓값을 꺼내고, 해당 ID를 삭제 마킹
                        _, idx = heapq.heappop(max_pq)
                        is_deleted[idx] = True

                else:           # 최솟값 삭제
                    # 힙의 탑에 있는 원소의 ID가 이미 삭제된 것이라면 청소
                    while min_pq and is_deleted[min_pq[0][1]]:
                        heapq.heappop(min_pq)
                    if min_pq:
                        # 진짜 살아있는 최솟값을 꺼내고, 해당 ID를 삭제 마킹
                        _, idx = heapq.heappop(min_pq)
                        is_deleted[idx] = True

        # 모든 명령어가 끝난 후, 힙의 상단에 남아있는 '이미 지워진 유효하지 않은 원소' 최종 청소
        while max_pq and is_deleted[max_pq[0][1]]:
            heapq.heappop(max_pq)
        while min_pq and is_deleted[min_pq[0][1]]:
            heapq.heappop(min_pq)

        # 출력 조건 검사
        if not min_pq:  
            print("EMPTY")
        else:
            print(-max_pq[0][0], min_pq[0][0])


def solve_boj_1202():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    # 튜플로 받으면 리스트보다 메모리를 덜 먹어서 백준에서 아슬아슬한 메모리 제한 통과할 때 유리합니다.
    gems = [tuple(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    gems.sort() 
    bags.sort()
    result = 0 
    tmp = []

    # gems 리스트의 현재 위치를 가리킬 포인터 변수
    gem_idx = 0

    for bag in bags:
        # gems 배열을 직접 pop하지 않고, 인덱스가 범위를 안 벗어났는지만 체크!
        while gem_idx < n and gems[gem_idx][0] <= bag:
            heapq.heappush(tmp, -gems[gem_idx][1])
            gem_idx += 1  # 보석을 소모하지 않고 포인터만 한 칸 전진 (O(1))
        
        if tmp:
            result -= heapq.heappop(tmp)
    
    print(result)


# Week10 | Binary-Search & Paramatric Search


# Week11, Week12 | Dynamic Programming Advanced


# Week13 | Simulation


if __name__ == '__main__':
    solve_boj_1202()