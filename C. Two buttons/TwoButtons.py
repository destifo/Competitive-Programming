from collections import deque


nums = list(map(int, input().split()))

qu = deque()
qu.append(nums[0])
depth = -1
target = nums[1]
vstd = set()

while qu:
    depth +=1
    n = len(qu)
    for i in range(n):
        nod = qu.popleft()
        if nod in vstd: continue
        vstd.add(nod)
        
        if nod == target:
            print(depth)
            quit()
        
        if nod < target:
            qu.append(nod*2)
        if nod > 0:
            qu.append(nod-1)
        