from collections import deque
from typing import *


def buildGraph(edges):
    graph = {}
    for edge in edges:
        nod1, nod2 = edge
        if not nod1 in graph.keys():
            graph[nod1] = []
        if not nod2 in graph.keys():
            graph[nod2] = []
        graph[nod1].append(nod2)
        graph[nod2].append(nod1)
        
    return graph



def isWinnable(cordrs: List[int], friends: List[int]) -> None:
    graph = buildGraph(cordrs)
    qu1 = deque()
    qu1.append(1)
    qu2 = deque()
    for i in range(len(friends)):
        qu2.append(friends[i])
    vstd = set()
    vstd1 = set()
    
    while qu1 and qu2:
        n = len(qu2)
        for i in range(n):
            nod = qu2.popleft()
            if nod in vstd: continue
            vstd.add(nod)
            
            for nb in graph[nod]:
                qu2.append(nb)
                
        m = len(qu1)
        for j in range(m):
            nod = qu1.popleft()
            if nod in vstd1 or nod in vstd:    continue
            vstd1.add(nod)
            
            if nod != 1 and nod not in vstd and len(graph[nod]) == 1:
                print('YES')
                return
            
            for nb in graph[nod]:
                qu1.append(nb)
                
                
    print('NO')



t = int(input())
for i in range(t):
    blank = input()
    n, k = list(map(int, input().split()))
    friends = list(map(int, input().split()))
    cordrs = []
    for j in range(n-1):
        cordr = list(map(int, input().split()))
        cordrs.append(cordr)
    
    isWinnable(cordrs, friends)