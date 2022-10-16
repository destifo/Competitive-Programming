'''
https://leetcode.com/problems/sum-of-subarray-minimums/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(n) space
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        
        inc_stack = []
        
        def pushToStack(index:int, stack:list) -> int:
            tot = 0
            num = arr[index]
            while stack and num < arr[stack[-1]]:
                curr_i = stack.pop()
                prev_i = stack[-1] if stack else -1
                tot += (curr_i - prev_i) * (i - curr_i) * (arr[curr_i])
                
            stack.append(i)
            
            return tot
        
        for i in range(n):
            ans += pushToStack(i, inc_stack)
         
        stack = inc_stack
        i = n
        while stack:
            curr_i = stack.pop()
            prev_i = stack[-1] if stack else -1
            ans += (curr_i - prev_i) * (i - curr_i) * (arr[curr_i])
                
        return ans % (10**9 + 7)

    
    # O(n) time,
    # O(n) space,
    # Approach: monotonic stack, arra
    def sumSubarrayMins2(self, arr: List[int]) -> int:
        
        def findSubarrayMinSum(nums: List[int]) -> int:
            tot = 0
            stack = [] # monotonic(non decreasing) stack
            
            for index, num in enumerate(nums):
                while stack and num <= nums[stack[-1]]:
                    popped_index = stack.pop()
                    left_offset = stack[-1] if stack else -1
                    right_offset = index
                    num_subarrays = (popped_index-left_offset) * (right_offset-popped_index)
                    tot += nums[popped_index] * num_subarrays
                stack.append(index)
            
            right_offset = len(nums)
            while stack:
                popped_index = stack.pop()
                left_offset = stack[-1] if stack else -1
                num_subarrays = (popped_index-left_offset) * (right_offset-popped_index)
                tot += nums[popped_index] * num_subarrays
                
            return tot
        
        return findSubarrayMinSum(arr) % (10**9 + 7)


sol = Solution()
print(sol.sumSubarrayMins([3,1,2,4]))