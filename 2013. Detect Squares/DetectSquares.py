from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.point_cnt_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_cnt_map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for x, y in list(self.point_cnt_map):
            
            if (abs(x - px) == abs(y - py)) and x != px and y != py:
                
                res += (
                    self.point_cnt_map[(x, y)]
                    * self.point_cnt_map[(x, py)]
                    * self.point_cnt_map[(px, y)]
                )

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)