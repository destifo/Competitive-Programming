'''
https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1
'''

class Solution:

    def count_zeros_infactorial_of(self, num:int):
        denom = 5
        zero_count = 0

        while num >= denom:
            qutnt = num // denom
            zero_count +=qutnt
            denom *=5

        return zero_count


    def findNum(self, n : int):
        # Complete this function
        low = 0
        high = n * 5

        def binarySearch(start, end):
            ans = end
            repitition = 0
            while (start < end):
                mid = (start + end) // 2
                zero_count = self.count_zeros_infactorial_of(mid)

                if zero_count >= n:
                    ans, end = mid, mid
                else:
                    start = mid

                if end - start < 2:
                    if repitition == 1: break
                    repitition +=1

            return ans

        return binarySearch(low, high)
                 


sol = Solution()
print(sol.findNum(25))