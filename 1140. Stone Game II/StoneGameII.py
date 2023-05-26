from typing import Dict, List, Tuple


class Solution:
    
    def take(self, index: int, piles: List[int], m: int, alice_turn: bool, memo: Dict[Tuple[int], int]) -> Tuple[int]:
        
        if index == len(piles):
            return 0, 0
        
        if (index, alice_turn, m) in memo:
            return memo[(index, alice_turn, m)]
        
        alice = 0
        bob = 0
        
        limit = (2*m) + 1
        for i in range(1, limit):
            if index+i >= len(piles):
                break
            curr_alice = piles[index+i] - piles[index]
            curr_bob = curr_alice
            next_alice, next_bob = self.take(index+i, piles, max(m, i), not alice_turn, memo)
            curr_alice += next_alice
            curr_bob += next_bob
            if alice_turn and curr_alice > alice:
                alice = curr_alice
                bob = next_bob
            
            if not alice_turn and curr_bob > bob:
                alice = next_alice
                bob = curr_bob
            
        memo[(index, alice_turn, m)] = (alice, bob)
        return alice, bob
    
    
    # O(n^2) time,
    # O(n) space,
    # Approach: min-max algorithm, dp, prefix sum, 
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sum = [0]
        tot = 0
        for pile in piles:
            tot += pile
            prefix_sum.append(tot)
        
        return self.take(0, prefix_sum, 1, True, {})[0]