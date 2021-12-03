import copy
from collections import deque

volume = list(map(int, input().split()))
d = [[[False]*201 for _ in range(201)] for _ in range(201)]

q = deque()
answer = set()
q.append([0, 0, volume[-1]])
d[0][0][volume[-1]] = True

while q:
    cur = q.popleft()

    if cur[0] == 0:
        answer.add(cur[-1])

    for i in range(3):
        if cur[i] > 0:
            for j in range(3):
                if i == j:
                    continue
                if cur[j] == volume[j]:
                    continue

                temp = copy.deepcopy(cur)
                print("before: ", temp)
                while (volume[j] - temp[j] > 0) and (temp[i] > 0):
                    temp[i] -= 1
                    temp[j] += 1
                print(i, j, temp)
                if not d[temp[0]][temp[1]][temp[2]]:
                    d[temp[0]][temp[1]][temp[2]] = True
                    q.append([temp[0], temp[1], temp[2]])

answer = list(answer)
answer.sort()
print(*answer, sep=' ')







# 8 9 10