class Solution:
    def isValidNum(self, num: int, index: int, n: int, max_sum: int) -> bool:
        if num > index:
            max_sum -= (num + num - index) * (index + 1) // 2
        else:
            max_sum -= (num + 1) * (num) // 2 + index - num + 1

        if num >= n - index:
            max_sum -= (num + num - n + 1 + index) * (n - index) // 2
        else:
            max_sum -= (num + 1) * num // 2 + n - index - num

        max_sum += num
        return max_sum >= 0

    # O(log(maxSum)) time,
    # O(1) space,
    # Approach: binary search, greedy,
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        average = maxSum // n
        lo, hi = 1, maxSum
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.isValidNum(mid, index, n, maxSum):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans % (10**9 + 7)
