from collections import Counter
import math


class Solution:
    # O(m) time, m --> number of digits in n
    # O(m) space,
    # Approach: hashtable,
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        n_count = Counter(str_n)
        start_exp = math.log((10**(len(str_n)-1)), 2)
        start_exp = int(math.ceil(start_exp))
        end_exp = math.log((10**(len(str_n))), 2)
        end_exp = int(math.ceil(end_exp))
        # print(start_exp, end_exp)
        
        for exp in range(start_exp, end_exp):
            num = (2**exp)
            num_count = Counter(str(num))
            if n_count == num_count:
                return True
            
        return False