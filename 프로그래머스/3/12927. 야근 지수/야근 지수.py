import heapq

def solution(n, works):

    if sum(works) <= n:
        return 0

    heap = []

    for work in works:
        heapq.heappush(heap, -work)

    for _ in range(n):
        biggest = -heapq.heappop(heap)
        biggest -= 1
        heapq.heappush(heap, -biggest)

    answer = 0

    for work in heap:
        answer += (-work) ** 2

    return answer