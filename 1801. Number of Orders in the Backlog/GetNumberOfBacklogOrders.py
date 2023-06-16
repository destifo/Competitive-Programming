import heapq
from typing import List


class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap,
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        sell_log = []
        buy_log = []
        in_log = 0

        for order in orders:
            price, amount, order_type = order
            amount %= MOD
            if order_type == 0:
                while amount > 0 and sell_log and sell_log[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_log)
                    left_sell = max(0, sell_amount - amount)
                    if left_sell > 0:
                        heapq.heappush(sell_log, (sell_price, left_sell))
                    in_log -= min(amount, sell_amount)
                    amount = max(0, amount - sell_amount)
                if amount > 0:
                    heapq.heappush(buy_log, (-price, amount))
                    in_log += amount
            else:
                while amount > 0 and buy_log and -buy_log[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_log)
                    left_buy = max(0, buy_amount - amount)
                    if left_buy > 0:
                        heapq.heappush(buy_log, (buy_price, left_buy))
                    in_log -= min(amount, buy_amount)
                    amount = max(0, amount - buy_amount)
                if amount > 0:
                    heapq.heappush(sell_log, (price, amount))
                    in_log += amount

        return in_log % MOD
