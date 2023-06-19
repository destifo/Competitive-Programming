from collections import deque


class Solution:
    
    # O(logn) time,
    # O(logn) space,
    # Approach: greedy, string,
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        digits = deque()
        digits.append(s[0])
        
        i = 1
        while i < len(s):
            digits.append(s[i])
            if int(s[i]) < int(s[i-1]):
                break
            i += 1

        if i == len(s):    return n

        while i > 0 and int(digits[i]) < int(digits[i-1]):
            i -= 1
            digits[i] = str(int(digits[i])-1)
        while digits and int(digits[0]) == 0:
            digits.popleft()
        digits = list(digits)
        ans = "".join(digits[:i+1]) + (len(str(n))-i-1)*'9'
        
        return int(ans)