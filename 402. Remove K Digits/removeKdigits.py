from django.forms import IntegerField
from numpy import integer


class Solution:
    def removeKdigits1(self, num, k):#works only for removal of contigious numbers
        n = len(num)
        if (k == n): return num
        i = 0
        j = k - 1
        result = float('inf')
        while j < n:
            spliced_num = num[0:i] + (num[j + 1: n])
            result = min(int(spliced_num), result)
            i +=1 
            j +=1 
        
        return str(int(result))
    

    def removeKdigits(self, num, k):
        n = len(num)
        if (k == n):    return "0"
        result = []
        for digit in num:
            while len(result) != 0 and result[-1] > digit and k > 0:
                result.pop()
                k -=1
            result.append(digit)

        return str(int("".join(result[:n - k])))            
        
        

sol = Solution()
print(sol.removeKdigits("112", 1))