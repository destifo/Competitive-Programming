from collections import defaultdict
import heapq
from typing import List


class Solution:
    
    def addToHeap(self, point, heap, graph, visited):
        for edge in graph[point]:
            dist, end = edge
            if end in visited:
                continue
            heapq.heappush(heap, edge)
    
    
    # O(len(points)^2) time,
    # O(len(points)^2) space,
    # Approah: prim's algo, heap, greedy, min spaning tree
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build all the edges
        graph = defaultdict(list)
        smallest_edge = None
        min_dist = float('inf')
        
        for i in range(len(points)):
            curr_point = tuple(points[i])
            for j in range(i+1, len(points)):
                nbr_point = tuple(points[j])
                dist = abs(curr_point[0]-nbr_point[0]) + abs(curr_point[1]-nbr_point[1])
                if dist < min_dist:
                    min_dist = dist
                    smallest_edge = (curr_point, nbr_point)
                
                graph[curr_point].append((dist, nbr_point))
                graph[nbr_point].append((dist, curr_point))
        
        
        # start from the smallest edge and build a tree,
        # each time we need to take the shortest edge,
        # the edge sld always add a new node,
        visited = set()
        min_heap = []
        point1, point2 = smallest_edge
        visited.add(point1)
        visited.add(point2)
        
        self.addToHeap(point1, min_heap, graph, visited)
        self.addToHeap(point2, min_heap, graph, visited)
        
        tot_cost = 0
        while len(visited) < len(points):
            dist, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            tot_cost += dist
            visited.add(point)
            self.addToHeap(point, min_heap, graph, visited)
            
        return tot_cost
    

    def find(self, node, parent):
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1, node2, parent, size):
        
        parent1 = parent[node1]
        parent2 = parent[node2]
        
        if parent1 < parent2:
            size[parent1] += size[parent2]
            size[parent2] = 0
            parent[parent2] = parent1
        else:
            size[parent2] += size[parent1]
            size[parent1] = 0
            parent[parent1] = parent2
    
    
    # O(len(points)^2) time,
    # O(len(points)^2) space,
    # Approach: kruskal algo, union find, heap, min spaning tree
    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        min_heap = []
        index_of = {}
        
        for i in range(len(points)):
            point1 = tuple(points[i])
            index_of[point1] = i
            for j in range(i+1, len(points)):
                point2 = tuple(points[j])
                dist = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
                heapq.heappush(min_heap, (dist, point1, point2))
                
        parent = [i for i in range(len(points))]
        size = [1 for _ in range(len(points))]
        
        tot_cost = 0
        while size[0] < len(points) and min_heap:
            dist, point1, point2 = heapq.heappop(min_heap)
            if self.find(index_of[point1], parent) == self.find(index_of[point2], parent):
                continue
                
            tot_cost += dist
            self.union(index_of[point1], index_of[point2], parent, size)
            
        return tot_cost