from collections import deque


adj_lst = {}

n = int(input())
for i in range(n):
    repost = input().split()
    if repost[2].lower() not in adj_lst.keys():
        adj_lst[repost[2].lower()] = []
        
    adj_lst[repost[2].lower()].append(repost[0].lower())
    

qu = deque()
qu.append('polycarp')

depth = 0

while qu:
    depth +=1
    n = len(qu)
    
    for i in range(n):
        nod = qu.popleft()
        
        if nod in adj_lst.keys():
            for nb in adj_lst[nod]:
                qu.append(nb)
            
print(depth)
    
