from collections import defaultdict
from typing import List


class Solution:
    
    def find(self, email: str, parent) -> str:
        
        if email != parent[email]:
            parent[email] = self.find(parent[email], parent)
            
        return parent[email]
    
    
    def union(self, email1: str, email2: str, parent) -> None:
        if email1 not in parent:
            parent[email1] = email2
        else:
            self.find(email2, parent)
            parent[parent[email2]] = self.find(email1, parent)
    
    # O(nlogn) time, n -> number of emails
    # O(n) space,
    # Approach: Union find, dfs
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        owner = {}
        parent = {}
        children = defaultdict(list)
        
        merged_accounts = []
        
        for account in accounts:
            # account = acc.split(',')
            # print(account)
            name = account[0]
            root = account[1]
            owner[root] = name
            
            for i in range(1, len(account)):
                self.union(account[i], root, parent)
                
        for email in parent:
            self.find(email, parent)
            children[parent[email]].append(email)
            
        for p in children:
            merged_account = []
            merged_account.append(owner[p])
            children[p].sort()
            
            for child in children[p]:
                merged_account.append(child)
                
            merged_accounts.append(merged_account)
        
        # print(parent)
        return merged_accounts