class Solution:
    def containsDuplicate(self, nums):
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False

    def containsDuplicateBySorting(self, nums):
        nums.sort()
        
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False