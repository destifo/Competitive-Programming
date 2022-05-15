'''
https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
'''

class Solution:
    # jeez, ugly code, gotta make it better later on
    def minimumBuckets(self, street: str):
        n = len(street)
        if n == 1 and street[0] == 'H':  return -1
        bucketsIndices = [False] * n

        for i in range(n):
            if street[i] == '.':
                continue
            
            if i == 0:
                if street[1] == 'H':
                    return -1
                bucketsIndices[1] = True
                continue

            if i == n - 1:
                if street[n - 2] == 'H':
                    return -1

                if not bucketsIndices[n - 2]:
                    bucketsIndices[n - 2] = True
                continue
            
            if street[i - 1] == 'H' and street[i + 1] == 'H':
                return -1
            elif street[i - 1] == 'H':
                bucketsIndices[i + 1] = True
            elif street[i + 1] == 'H' and not bucketsIndices[i - 1]:
                bucketsIndices[i - 1] = True
            elif not bucketsIndices[i - 1]:
                bucketsIndices[i + 1] = True

        ans = 0
        for i in range(n):
            if bucketsIndices[i]:
                ans +=1

        return ans          


sol = Solution()
print(sol.minimumBuckets(".HH.H"))