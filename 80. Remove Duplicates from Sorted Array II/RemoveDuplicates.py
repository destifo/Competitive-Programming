class Solution:
    # some questions drive u crazy, needed help for real
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:   return
        l, r = 2, 2
        
        while r < n:
            if nums[l-2] != nums[r]:
                nums[l] = nums[r]
                l +=1
            r +=1
            
        return l


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))