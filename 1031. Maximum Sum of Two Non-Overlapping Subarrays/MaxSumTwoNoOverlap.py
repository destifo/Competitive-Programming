'''
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
'''

import heapq
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int):
        n = len(nums)
        prefixSum = [0]*(n + 1)
        currSum = 0
        for i in range(n):
            currSum +=nums[i]
            prefixSum[i + 1] = currSum

        def findMax( prefixSum, firstLen, secondLen):
            n = len(prefixSum) - 1
            l, r = 1, firstLen
            index1, index2 = l, r
            first_max = 0
            while r <= n:
                currSum = prefixSum[r] - prefixSum[l - 1]
                if currSum > first_max:
                    first_max = currSum
                    index1, index2 = l, r
                l, r = l + 1, r + 1

            second_max = 0
            if index1 >= secondLen - 1 and n - index2 >= secondLen:
                l, r = 1, secondLen
                while r < index1:
                    currSum = prefixSum[r] - prefixSum[l - 1]
                    second_max = max(second_max, currSum)
                    l, r = l + 1, r + 1

                l, r = index2 + 1, index2 + secondLen
                while r <= n:
                    currSum = prefixSum[r] - prefixSum[l - 1]
                    second_max = max(second_max, currSum)
                    l, r = l + 1, r + 1
            elif index1 >= secondLen - 1:
                l, r = 1, secondLen
                while r < index1:
                    currSum = prefixSum[r] - prefixSum[l - 1]
                    second_max = max(second_max, currSum)
                    l, r = l + 1, r + 1
            else:
                l, r = index2 + 1, index2 + secondLen
                while r <= n:
                    currSum = prefixSum[r] - prefixSum[l - 1]
                    second_max = max(second_max, currSum)
                    l, r = l + 1, r + 1

            return first_max + second_max

        return max(findMax(prefixSum, firstLen, secondLen), findMax(prefixSum, secondLen, firstLen))


    # this is the working solution
    def maxSumTwoNoOverlap2(self, nums, firstLen: int, secondLen: int):
        n = len(nums)
        prefixSum = [0]*(n + 1)
        currSum = 0
        for i in range(n):
            currSum +=nums[i]
            prefixSum[i + 1] = currSum

        firstMax = []
        secondMax = []
        for i in range(firstLen, n + 1):
            val = prefixSum[i] - prefixSum[i - firstLen]
            firstMax.append((i - firstLen + 1, i, val))

        for i in range(secondLen, n + 1):
            val = prefixSum[i] - prefixSum[i - secondLen]
            secondMax.append((i - secondLen + 1, i, val))

        maxheap = []
        for val1 in firstMax:
            index1, index2 = val1[0], val1[1]
            for val2 in secondMax:
                index3, index4 = val2[0], val2[1]
                if ((index3 < index1 and index4 < index1) or (index3 > index2 and index4 > index2)):
                    # print(index1, index2)
                    # print(index3, index4)
                    # print(key1 + key2)
                    heapq.heappush(maxheap, -1 * (val1[2] + val2[2]))

        return -1 * maxheap[0]

    
    # O(n^2) time,
    # O(1) space,
    # Approach: prefix sum
    def maxSumTwoNoOverlap3(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        max_sum = 0
        
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        def findSubarraySum(l: int, r: int) -> int:
            if l == 0:
                return nums[r]
            
            return nums[r] - nums[l-1]
        
        for i in range(0, n-firstLen+1):
            first_tot = findSubarraySum(i, i+firstLen-1)
            for j in range(0, i-secondLen+1):
                second_tot = findSubarraySum(j, j+secondLen-1)
                max_sum = max(max_sum, second_tot + first_tot)
                
            for j in range(i+firstLen, n-secondLen+1):
                second_tot = findSubarraySum(j, j+secondLen-1)
                max_sum = max(max_sum, second_tot + first_tot)
                
        return max_sum


sol = Solution()
print(sol.maxSumTwoNoOverlap2([1,0,1],1,1))