class Solution:
    
    # O(digits) time,
    # O(digits^2) space,
    # Approach: brute force, string
    def maximumSwap(self, num: int) -> int:
        digit_list = list(digit for digit in str(num))
        
        max_num = num
        for i in range(len(digit_list)):
            for j in range(i+1, len(digit_list)):
                digit_list[i], digit_list[j] = digit_list[j], digit_list[i]
                new_num = int("".join(digit_list))
                max_num = max(max_num, new_num)
                digit_list[j], digit_list[i] = digit_list[i], digit_list[j]
        
        return max_num