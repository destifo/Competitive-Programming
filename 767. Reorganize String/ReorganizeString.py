from collections import Counter, deque
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
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, queue, string, 
    def reorganizeString2(self, s: str) -> str:
        count = Counter(s)
        heap = []
        
        for ch, cnt in count.items():
            heapq.heappush(heap, (-cnt, ch))
            
        str_builder = []
        waiting_char = None
        waiting_count = 0
        while heap:
            cnt, ch = heapq.heappop(heap)
            cnt = -cnt
            
            if waiting_char and waiting_count:
                heapq.heappush(heap, (-waiting_count, waiting_char))
            cnt -= 1
            str_builder.append(ch)
            
            waiting_char = ch
            waiting_count = cnt
            
        return "".join(str_builder) if waiting_count == 0 else ""


sol = Solution()
print(sol.reorganizeString("aab"))