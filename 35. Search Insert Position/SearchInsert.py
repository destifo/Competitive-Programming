class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if target > nums[n-1]:  return n
        if target < nums[0]:    return 0
        
        def binary_search(start, end):
            mid = (start + end)//2
            if target == nums[mid]:
                return mid
            if (mid+1) < n and target > nums[mid] and target <= nums[mid+1]:
                return mid + 1
            if target > nums[mid]:
                # if (mid+1) and target > nums[mid+1]:
                #     start = mid+1
                # else:
                start = mid
            else:
                end = mid

                
            return binary_search(start, end)

        return binary_search(0, n-1)
            

sol = Solution()
print(sol.searchInsert([1,3,5,6]
,4))