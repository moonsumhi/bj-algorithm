from collections import deque

INF=9876543210
maxNum=52


def toNum(alpa):
    if ord(alpa)<=ord('Z'):
        return ord(alpa)-ord('A')
    else:
        return ord(alpa)-ord('a')+26

def findMin(node):
    global minFlow
    if node==0:
        return

    rest=c[prev[node]][node]-flow[prev[node]][node]
    if rest<minFlow:
        minFlow=rest
    findMin(prev[node])

def makeFlow(node):
    if node==0:
        return
    flow[prev[node]][node]+=minFlow
    flow[node][prev[node]]-=minFlow

    makeFlow(prev[node])

N=int(input())
graph={}
c=[[0 for j in range(maxNum)] for i in range(maxNum)]
flow=[[0 for j in range(maxNum)] for i in range(maxNum)]
totalFlow=0
fin=toNum('Z')

for i in range(maxNum):
    graph[i]=[]

for i in range(N):
    a,b,cost=input().split()
    numA=toNum(a)
    numB=toNum(b)
    cost=int(cost)

    c[numA][numB] += cost
    c[numB][numA] += cost
    graph[numA].append(numB)
    graph[numB].append(numA)

while(1):
    prev=[-1 for i in range(maxNum)]
    q=deque([0])
    while(q):
        now=q.popleft()

        if now==fin:
            break

        for next in graph[now]:
            if (c[now][next]-flow[now][next])>0 and prev[next]==-1:
                q.append(next)
                prev[next]=now

    #한번 돌았는데 z까지 못가면?
    if prev[fin]==-1:
        break

    #A에서 Z로 가는 경로 중 가장 작은 용량?
    minFlow=INF
    findMin(fin)
    #경로상의 가장 작은양(min_flow)만큼 물을 흘림, 반대방향으론 -만큼
    makeFlow(fin)

    totalFlow+=minFlow



print(totalFlow)