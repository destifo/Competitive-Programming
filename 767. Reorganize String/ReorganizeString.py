from collections import deque
import heapq


class Solution:
    def reorganizeString(self, s: str):
        letter_count = {}
        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        maxHeap = []
        waiting_queue = deque()
        for key, val in letter_count.items():
            heapq.heappush(maxHeap, (-val, key))

        ans = ""
        while maxHeap:
            curr = heapq.heappop(maxHeap)
            count = -curr[0]
            ans +=curr[1]
            if waiting_queue:
                heapq.heappush(maxHeap, waiting_queue.popleft())
            count -=1
            if count:   waiting_queue.append((-count, curr[1]))
        
        if waiting_queue:   return ""
        return ans


sol = Solution()
print(sol.reorganizeString("aab"))