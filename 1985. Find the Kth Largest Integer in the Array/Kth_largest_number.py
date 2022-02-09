"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
"""

class Solution:

    def merge(self, first, second, result):
        i = 0
        j = 0 
        k = 0
        while (i < len(first) and j < len(second)):
            if (int(first[i]) >= int(second[j])):
                result[k] = first[i]
                k +=1
                i +=1
            else:
                result[k] = second[j]
                k +=1
                j +=1
        while (j < len(second)):
            result[k] = second[j]
            k +=1
            j +=1
        while (i < len(first)):
            result[k] = first[i]
            k +=1
            i +=1
        
    def mergeSort(self, array):
        if (len(array) < 2):
            return
        middleIndex = len(array)//2
        left = [0] * middleIndex
        right = [0] * (len(array) - middleIndex)
        for i in range(middleIndex):
            left[i] = array[i]
        for i in range(len(array) - middleIndex):
            right[i] = array[middleIndex + i]

        self.mergeSort(left)
        self.mergeSort(right)

        self.merge(right, left, array)

    def kthLargestNumber(self, nums, k: int) -> str:
        self.mergeSort(nums)
        return nums[k - 1]
        
    

sol = Solution()
print(sol.kthLargestNumber(["0","1","1"], 1))