class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum, right_sum = 0, 0
        left_marks, right_marks = 0, 0
        
        for i, val in enumerate(num):
            if val.isdigit():
                if i < len(num)//2:    left_sum += int(val)
                else:   right_sum += int(val)
            else:
                if i < len(num)//2:    left_marks += 1
                else:   right_marks += 1
        
        if (right_marks + left_marks) % 2 == 1:
            return True
        
        left_pair = (left_sum, left_marks)
        right_pair = (right_sum, right_marks)
        
        larger, smaller = max(left_pair, right_pair), min(left_pair, right_pair)
        
        larger_sum, larger_marks = larger
        smaller_sum, smaller_marks = smaller
        if smaller_marks < larger_marks:    return True

        return not (smaller_sum + (smaller_marks-larger_marks)*9 / 2 == larger_sum)