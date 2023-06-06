from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, queue, 
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        index_of = defaultdict(deque)
        for i, task in enumerate(tasks):
            index_of[(task[0], task[1])].appendleft(i)
        
        tasks.sort(key=lambda x:x[0])
        curr_index = 0
        queue = []
        processesed_tasks = []
        time = 0
        while curr_index < len(tasks):
            while curr_index < len(tasks) and tasks[curr_index][0] <= time:
                index = index_of[(tasks[curr_index][0], tasks[curr_index][1])].pop()
                heapq.heappush(queue, (tasks[curr_index][1], index))
                curr_index += 1
            
            if queue:
                last_time, task = heapq.heappop(queue)
                time += last_time
                processesed_tasks.append(task)
            else:
                time = tasks[curr_index][0]
        
        while queue:
            last_time, task = heapq.heappop(queue)
            processesed_tasks.append(task)
        
        return processesed_tasks