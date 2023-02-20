class Solution:
    
    def isIPv4(self, s: str) -> bool:
        
        subnets = s.split(".")
        if len(subnets) != 4:
            return False

        for subnet in subnets:
            
            if not subnet.isdigit() or (len(subnet) > 1 and subnet[0] == "0") or (int(subnet) > 255 or int(subnet) < 0):
                return False
            
        return True
    
    
    def isIPv6(self, s: str) -> bool:
        
        subnets = s.split(":")
        
        if len(subnets) != 8:
            return False
        
        valid_vals = {"a", "b", "c", "d", "e", "f"}

        for subnet in subnets:
            if len(subnet) < 1 or len(subnet) > 4:
                return False
            
            for ch in subnet:
                if not ch.isdigit() and (ch.lower() not in valid_vals):
                    return False
        
        return True
    
    
    # O(n) time,
    # O(1) space,
    # Approach: string
    def validIPAddress(self, queryIP: str) -> str:
        
        if self.isIPv4(queryIP):
            return "IPv4"
        
        if self.isIPv6(queryIP):
            return "IPv6"
        
        return "Neither"