from collections import deque
import copy

MAX_SHEEP = 0

class Node():
    def __init__(self, key):
        self.key = key
        self.sheep = 0
        self.wolf = 0
        self.parent = None
        self.children = []


def traversal(sales, node):
    Cost[node][0] = 0
    Cost[node][1] = sales[node]

    if not Children[node]:
        return

    extraCost = math.inf
    for child in Children[node]:
        traversal(sales, child)
        if Cost[child][0] < Cost[child][1]:
            Cost[node][0] += Cost[child][0]
            Cost[node][1] += Cost[child][0]
            extraCost = min(extraCost, Cost[child][1] - Cost[child][0])
        else:
            Cost[node][0] += Cost[child][1]
            Cost[node][1] += Cost[child][1]
            extraCost = 0
    Cost[node][0] += extraCost

def dfs(start, nodes, s, w):
    global MAX_SHEEP
    print(start, s, w)
    MAX_SHEEP = max(MAX_SHEEP, s)

    if nodes[start].children == []:
        return

    for child in nodes[start].children:
        next_s, next_w = s+nodes[child].sheep, w+nodes[child].wolf
        if next_s <= next_w:
            continue
        else:
            nodes[child].sheep -= 1
            nodes[child].wolf -= 1
            dfs(child, nodes, next_s, next_w)
            nodes[child].sheep += 1
            nodes[child].wolf += 1







def solution(info, edges):
    global MAX_SHEEP
    answer = 0
    nodes = [Node(i) for i in range(len(info))]

    for i in range(len(info)):
        if info[i] == 0:
            nodes[i].sheep = 1
        else:
            nodes[i].wolf = 1

    for i in edges:
        p, c = i
        nodes[p].children.append(c)
        nodes[c].parent = nodes[p].key

    dfs(0, nodes, nodes[0].sheep, nodes[0].wolf)
    print(MAX_SHEEP)






    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])