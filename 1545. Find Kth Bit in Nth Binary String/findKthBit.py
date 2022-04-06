'''
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/
'''

class Solution:
    # worked on first try...:-)
    def invert(self, strg):
        final_lst = []
        for ch in strg:
            if ch == '0':
                final_lst.append("1")
            else:
                final_lst.append("0")

        return "".join(final_lst)

    def findSn(self, n):
        if n == 1:
            return "0"

        prevS = self.findSn(n - 1)
        return  prevS + "1" + self.invert(prevS)[::-1]

    def findKthBit(self, n: int, k: int):
        bit_str = self.findSn(n)
        return bit_str[k - 1]


sol = Solution()
print(sol.findKthBit(4, 11))