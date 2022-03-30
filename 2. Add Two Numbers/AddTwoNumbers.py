class Solution:
    def addTwoNumbers(self, l1, l2):
        max_len = len(l1) if (len(l1) > len(l2)) else len(l2)
        min_len = len(l1) if (len(l1) < len(l2)) else len(l2)
        result = [0]*max_len
        add_count = 0
        isL1larger = len(l1) > len(l2)
        left_over = 0
        for i in range(0, min_len):
            if (left_over != 0):
                tot = l1[i] + l2[i] + 1
            else:
                tot = l1[i] + l2[i]
            if (tot >= 10):
                left_over = 1
                tot = tot % 10
            else:
                left_over = 0

            result[i] = tot
            add_count += 1
        
        if left_over != 0 and add_count == max_len:
            result.append(1)

        if (add_count != max_len):
            for i in range(min_len, max_len):
                if left_over != 0:
                    result[i] = 1
                if (isL1larger):
                    result[i] += l1[i]
                else:
                    result[i] += l2[i]
                if (result[i] >= 10):
                        result[i] = result[i] % 10
                        left_over = 1
                else:
                    left_over = 0
                
        if left_over != 0:
            result.append(1)
            
        return result


sol = Solution()
print(sol.addTwoNumbers([9,9,9,9,9,9,9], l2 = [9,9,9,9]))