import heapq

N = int(input())

left_heap = []
right_heap = []
answer = []
for i in range(N):
    inputNum = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-inputNum, inputNum))
    else:
        heapq.heappush(right_heap, (inputNum, inputNum))

    if right_heap and left_heap[0][1] > right_heap[0][0]:
        min = heapq.heappop(right_heap)[0]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))
    answer.append(left_heap[0][1])

for i in answer:
    print(i)




# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5