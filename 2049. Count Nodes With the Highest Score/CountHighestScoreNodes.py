class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: DFS, Array
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        scores = []
        children = [[] for i in range(n)]
        
        for child, parent in enumerate(parents):
            if child == 0:  continue
            children[parent].append(child)
        
        def dfs(root:int) -> int:
            n = len(parents)
            if len(children[root]) == 0:
                scores.append(n - 1)
                return 1
            
            if len(children[root]) == 2:
                childrn = children[root]
                subtree1_size = dfs(childrn[0])
                subtree2_size = dfs(childrn[1])
                size_from_root = subtree1_size + subtree2_size + 1
                rest_size = n - size_from_root
                if rest_size == 0:  rest_size = 1
                scores.append(subtree1_size * subtree2_size * rest_size)
                return size_from_root
            
            else:
                child = children[root][0]
                subtree_size = dfs(child)
                size_from_root = subtree_size + 1
                rest_size = n - size_from_root
                if rest_size == 0:  rest_size = 1
                scores.append(subtree_size * rest_size)
                
                return size_from_root
            
        dfs(0)
        max_score = 0
        for score in scores:
            max_score = max(max_score, score)
        
        count = 0
        for score in scores:
            if score == max_score:
                count +=1
                
        return count


sol = Solution()
print(sol.countHighestScoreNodes([-1,3,3,5,7,6,0,0]))