'''
https://leetcode.com/problems/next-greater-element-iii/
'''


class Solution:
    # O(1) time
    # O(1) space
    def nextGreaterElement(self, n: int) -> int:
        str_int = str(n)
        digits = []
        present_digits = set()
        
        for digit in str_int:
            digits.append(digit)
            present_digits.add(int(digit))
            
        m = len(digits)
        def find_tobe_updated(digits:list[str]) -> int:
            prev = int(digits[-1])
            for i in range(m-2,-1,-1):
                curr = int(digits[i])
                if prev > curr:
                    return i
                prev = curr
            
            return len(digits)
        
        def find_next_greater_num(num) -> int:
            curr = num + 1
            while curr not in present_digits:
                curr +=1
                
            return curr
        
        
        def sort_leftout(digits, start) -> None:
            if len(digits) - start < 2:
                return
            
            to_be_sorted = digits[start:]
            to_be_sorted.sort()
            
            digits[start:] = to_be_sorted
            
        
        def is_overflowed(num:int) -> bool:
            if(abs(num) > (2 ** 31 - 1)):
                    return True
            else:
                False
            
        index = find_tobe_updated(digits)
        if index == len(digits):    return -1
        
        # print(digits[index])
        next_num = find_next_greater_num(int(digits[index]))
        # print(next_num)
        index2 = next((i for i in range(index, len(digits)) if int(digits[i]) == next_num), None)
        while not index2:
            next_num +=1
            index2 = next((i for i in range(index, len(digits)) if int(digits[i]) == next_num), None)
        
        temp = digits[index]
        digits[index] = digits[index2]
        digits[index2] = temp
        
        sort_leftout(digits, index+1)
        ans = "".join(digits)
        if is_overflowed(int(ans)):
            return -1
        
        return ans