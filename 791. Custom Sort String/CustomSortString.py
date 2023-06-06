'''
https://leetcode.com/problems/custom-sort-string/
'''


class Solution:
    # O(n) time, depends on our string s
    # O(1) space, we are just storing alphabets in a map so 26 len is constant
    # Approach: Hashmap, sorting
    def customSortString(self, order: str, s: str) -> str:
        n = len(order)
        order_map = {}
        ch_count = {}
        ans = ""
        
        for ch in s:
            ch_count[ch] = ch_count.get(ch, 0) + 1
            if ch in order:
                order_map[ch] = order.index(ch) + 1
            else:
                order_map[ch] = n + 1
                
        sorted_str = sorted(order_map.items(), key=lambda x:x[1])
        
        for ch, weight in sorted_str:
            ans += (ch * ch_count[ch])
            
        return ans