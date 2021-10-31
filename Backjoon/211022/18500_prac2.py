from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def destroy(i, left):
    i, j = r-i, 0
    if left == 1:
        for k in range(c):
            if a[i][k] == "x":
                a[i][k] = "."
                j = k
                break

    else:
        for k in range(c-1, -1, -1):
            if a[i][k] == "x":
                a[i][k] = '.'
                j = k
                break

r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
n = int(input())
s = list(map(int, input().split()))
dq = deque()

left = 1
while n:
    index = s.pop(0)
    destroy(index, left)

    while dq:
        x, y = dq.popleft()
        bfs(x, y)

    left *= -1
    n -= 1

