class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: two pointers, array
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        l, r = 0, 2*k
        result = []
        
        while r < n:
            diff = r - l
            sub_str = s[l:l+k]
            result.append(sub_str[::-1])
            result.append(s[l+k:r])
            l += 2*k
            r += 2*k
        
        diff = r - l
        if diff > k:
            sub_str = s[l:l+k]
            result.append(sub_str[::-1])
            result.append(s[l+k:r])
        else:
            sub_str = s[l:r]
            result.append(sub_str[::-1])
            
        result = ''.join(result)
        return result