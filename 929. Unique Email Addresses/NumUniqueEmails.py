from typing import List


class Solution:
    
    # O(len(emails)*len(email)) time,
    # O(len(emails)*len(email)) space,
    # Approach: string, hashset, 
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split("@")
            plus_index = local.find("+")
            if plus_index != -1:
                local = local[:plus_index]
                
            spl_local = local.split(".")
            local = "".join(spl_local)
            final_email = local+"@"+domain
            unique_emails.add(final_email)
            
        return len(unique_emails)