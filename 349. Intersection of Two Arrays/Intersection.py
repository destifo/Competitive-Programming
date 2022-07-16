'''
https://leetcode.com/problems/intersection-of-two-arrays/
'''


from collections import Counter


class Solution:
    # O(mlogm + nlogn) time,
    # O(min_len) space
    # space efficent
    # approach: sorting, 
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        m = len(nums2)
        ans = []
        
        nums1.sort()
        nums2.sort()
        
        while nums1 and nums2:
            if nums2[-1] == nums1[-1]:
                num = nums1[-1]
                ans.append(num)
                while nums1[-1] == num:
                    nums1.pop()
                while nums2[-1] == num:
                    nums2.pop()
            elif nums2[-1] > nums1[-1]:
                nums2.pop()
            else:
                nums1.pop()
                
        return ans


    # O(n + m) time,
    # O(n+m) space,
    # time efficent
    # approach: hash table
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []

        for key in count1.keys():
            if key in count2.keys():
                ans.append()

        return ans