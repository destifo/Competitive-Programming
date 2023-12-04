class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, hash map
    def largestGoodInteger(self, num: str) -> str:
        window = {}
        left, right = 0, 2
        ans = ""
        for i in range(right):
            digit = int(num[i])
            window[digit] = window.get(digit, 0) + 1
        
        while right < len(num):
            right_digit = int(num[right])
            window[right_digit] = window.get(right_digit, 0) + 1
            right += 1
            
            if len(window) == 1:
                if not ans or int(ans) < int(num[left:right]):
                    ans = num[left:right]
            
            left_digit = int(num[left])
            window[left_digit] -= 1
            if window[left_digit] == 0:
                window.pop(left_digit)
            left += 1
            
        return ans