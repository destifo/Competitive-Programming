'''
https://leetcode.com/problems/online-stock-span/
'''


class StockSpanner:

    def __init__(self):
        self.stack = []

    # O(n) time, reading the data stream
    # O(n) space, for the dec monotonic stack
    def next(self, price: int) -> int:
        span = 1
        if not self.stack:
            self.stack.append((price, span))
            # self.spans.append(span)
            return span
        
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)