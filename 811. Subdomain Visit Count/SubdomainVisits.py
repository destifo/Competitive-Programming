from collections import defaultdict
from typing import List


class Solution:
    
    # O(n*m^2) time,
    # O(n*m) space,
    # Approach: hashmap, 
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            cpdomain_info = cpdomain.split()
            visits, cpdomains = cpdomain_info
            domains = cpdomains.split(".")
            
            cummulative_domain = ""
            for i in range(len(domains)-1, -1, -1):
                cummulative_domain = domains[i] + cummulative_domain
                domain_count[cummulative_domain] += int(visits)
                if i > 0:
                    cummulative_domain = "." + cummulative_domain
                
        answers = []
        for domain, tot_visits in domain_count.items():
            info = str(tot_visits) + " " + domain
            answers.append(info)
            
        return answers