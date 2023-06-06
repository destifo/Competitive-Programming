from collections import deque
from typing import List


class Solution:
    
    def getNeighbors(self, gene, bank):
        nbrs = []
        gene = [neucleotide for neucleotide in gene]
        neucleotides = ['A', 'C', 'G', 'T']
        
        for i, ch in enumerate(gene):
            # swap in the other gene traits at each index, 
            for neucleotide in neucleotides:
                if neucleotide == ch:
                    continue
                nbr = gene.copy()
                nbr[i] = neucleotide
                nbr = "".join(nbr)
                if nbr not in bank:
                    continue
                nbrs.append(nbr)
                bank.remove(nbr)

        return nbrs
    
    # O(len(bank)) time,
    # O(len(bank)) space,
    # Approach: bfs, graph
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        intution: do a bfs search, starting from startGene, where we move from one gene to another(neighbor, if neighbor in bank) node. if we can reach start endGene, we can return the depth of our bfs search, else -1
        '''
        
        # init queue, bank set, depth
        queue = deque()
        queue.append(startGene)
        bank = set(bank)
        if startGene in bank:
            bank.remove(startGene)
        depth = 0
        
        # do bfs search, if we find endGene then we can return depth
        while queue:
            n = len(queue)
            for _ in range(n):
                curr_gene = queue.popleft()
                if curr_gene == endGene:
                    return depth
                    
                for nbr in self.getNeighbors(curr_gene, bank):
                    queue.append(nbr)
                    
            depth += 1
        
        # return -1 if we can't reach endGene
        return -1