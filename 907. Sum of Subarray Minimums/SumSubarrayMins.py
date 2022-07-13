'''
https://leetcode.com/problems/sum-of-subarray-minimums/
'''


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


sol = Solution()
print(sol.sumSubarrayMins([3,1,2,4]))