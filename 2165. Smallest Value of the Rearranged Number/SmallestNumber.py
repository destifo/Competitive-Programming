'''
https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
'''

class Solution:
    def smallestNumber(self, num: int):
        if num == 0:
            return 0
            
        digitCount = [0] * 10
        numstr = str(num)
        for digit in numstr:
            try:
                digit = int(digit)
                digitCount[digit] +=1
            except:
                continue
        
        def findmin(isPositive):
            res = []
            for i in range(1, 10):
                while digitCount[i] > 0:
                    res.append(str(i))
                    digitCount[i] -=1

            ans = ""
            if isPositive:
                if digitCount[0] > 0:
                    ans += (res[0] + ("0" * digitCount[0]))
                    ans +="".join(res[1:])
                else:
                    ans = "".join(res)
                ans = int(ans)
            else:
                ans = "".join(reversed(res))
                if digitCount[0] > 0:
                    ans += ("0" * digitCount[0])
                ans = -1 * int(ans)

            return ans

        return findmin(num >= 0)
                    

sol = Solution()
print(sol.smallestNumber(137493562464))