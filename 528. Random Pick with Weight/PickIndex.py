class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        total_weight = sum(w)
        
        for index, weight in enumerate(w):
            freq = math.ceil((weight/total_weight) * 100)
            self.weights.extend([index for _ in range(freq)])
        

    def pickIndex(self) -> int:
        return random.choice(self.weights)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()