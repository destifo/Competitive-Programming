class Solution:
    def sortedSquares(self, nums: list[int]):
        # Trivial solution/ O(nlogn)
        ans = [(num**2) for num in nums]
        ans.sort()
        
        return ans

    def sortedSquares(self, nums: list[int]):
        # O(n) solution
        n = len(nums)
        l, r = None, None
        for index, num in enumerate(nums):
            if num >= 0:
                r = index
                l = index - 1
                break

        if l and l < 0:   return [(num**2) for num in nums]
        if r == None:   return [(nums[i] **2) for i in range(n-1, -1, -1)]
        
        ans = []
        while l >= 0 and r < n:
            if abs(nums[l]) < nums[r]:
                ans.append(nums[l]** 2)
                l -=1
            else:
                ans.append(nums[r]**2)
                r +=1

        while l >= 0:
            ans.append(nums[l] **2)
            l -=1
        while r < n:
            ans.append(nums[r] **2)
            r +=1

        return ans