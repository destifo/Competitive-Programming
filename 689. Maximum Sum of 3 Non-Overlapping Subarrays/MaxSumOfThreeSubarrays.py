class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        numOfSubarrs = n - k + 1
        sumAtIndex = [0] * numOfSubarrs
        currSum = 0

        for i in range(n):
            currSum +=nums[i]
            if i >= k:
                currSum -= nums[i - k]

            if (i >= k - 1):
                sumAtIndex[i - k + 1] = currSum
                
        leftMaxIndex = [0] * numOfSubarrs
        bigIndex = 0
        for i in range(numOfSubarrs):
            if sumAtIndex[i] > sumAtIndex[bigIndex]:
                bigIndex = i

            leftMaxIndex[i] = bigIndex
        
        rightMaxIndex = [0] * numOfSubarrs
        bigIndex = numOfSubarrs - 1
        for i in range(numOfSubarrs- 1, -1, -1):
            if sumAtIndex[i] >= sumAtIndex[bigIndex]:
                bigIndex = i

            rightMaxIndex[i] = bigIndex

        ans = [-1] * 3
        for i in range(k, numOfSubarrs - k):
            if ans[0] == -1 or (sumAtIndex[ans[0]] + sumAtIndex[ans[1]] + sumAtIndex[ans[2]]) < (sumAtIndex[leftMaxIndex[i - k]] + sumAtIndex[i] + sumAtIndex[rightMaxIndex[i + k]]):
                ans[0] = leftMaxIndex[i - k]
                ans[1] = i
                ans[2] = rightMaxIndex[i + k]

        return ans