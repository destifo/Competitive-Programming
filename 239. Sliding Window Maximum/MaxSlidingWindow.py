from collections import deque
import heapq
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: heap, hashmap, array, 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max_heap = []
        left, right = 0, k-1
        for i in range(right):
            heapq.heappush(max_heap, -nums[i])
            count[nums[i]] = count.get(nums[i], 0) + 1
            
        ans = []
        while right < len(nums):
            heapq.heappush(max_heap, -nums[right])
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            while max_heap and count.get(-max_heap[0], 0) == 0:
                heapq.heappop(max_heap)
                
            ans.append(-max_heap[0])
            count[nums[left]] -= 1
            left += 1
            right += 1
        
        return ans 
    
    
    # O(n) time,
    # O(n) space,
    # Approach: monotonic queue, array, 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left, right = 0, k-1
        for i in range(right):
            num = nums[i]
            # if the current/recent number is greater than the previous number, we pop them from left cause we can use the new value as the maximum
            while queue and queue[0] < num:
                queue.popleft()
            
            # then we add the current number to the queue as it might be the maximum number in the next windows, 
            queue.appendleft(num)
                
        ans = []
        while right < len(nums):
            num = nums[right]
            while queue and queue[0] < num:
                queue.popleft()
            
            queue.appendleft(num)
            ans.append(queue[-1])
            
            # if the current maximum is the number to be removed from the window, then we remove it from the queue as well, 
            if queue[-1] == nums[left]:
                queue.pop()
            left += 1
            right += 1
            
        return ans       