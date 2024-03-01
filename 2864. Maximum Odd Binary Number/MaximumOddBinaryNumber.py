class Solution:

    # O(n) time,
    # O(n) space,
    # Approach: greedy,
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        n = len(s)
        num = ["0" for _ in range(n)]
        num[-1] = "1"

        for i in range(ones - 1):
            num[i] = "1"

        return "".join(num)
