from typing import List


class Transaction:
    
    def __init__(self, name: str, timestamp: int, amount: int, city: str, detail: str) -> None:
        
        self.name = name
        self.timestamp = timestamp
        self.amount = amount
        self.city = city
        self.detail = detail


class Solution:
    
    def leftTimeViolation(self, txs: List['Transaction'], curr_index: int) -> bool:
        index = curr_index
        
        while curr_index > 0:
            if (txs[index].timestamp - txs[curr_index-1].timestamp) > 60:
                break
            
            if (txs[index].timestamp - txs[curr_index-1].timestamp) <= 60 and txs[index].name == txs[curr_index-1].name and txs[index].city != txs[curr_index-1].city:
                return True
            curr_index -= 1
            
        return False
    
    
    def rightTimeViolation(self, txs: List['Transaction'], curr_index: int) -> bool:
        index = curr_index
        
        while curr_index < len(txs)-1:
            if (txs[curr_index+1].timestamp - txs[index].timestamp) > 60:
                break
                
            if (txs[curr_index+1].timestamp - txs[index].timestamp) <= 60 and txs[curr_index+1].name == txs[index].name and txs[curr_index+1].city != txs[index].city:
                return True
            curr_index += 1
        
        return False
    
    
    # O(n^2) time,
    # O(n) space, 
    # Approach: sorting, class design
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid_transactions = []
        
        sorted_transactions = []
        for tx in transactions:
            name, timestamp, amount, city = tx.split(',')
            
            sorted_transactions.append(Transaction(name, int(timestamp), int(amount), city, tx))
            
        
        sorted_transactions.sort(key=lambda transaction:transaction.timestamp)
        
        
        for i in range(len(transactions)):
            transaction = sorted_transactions[i]
            
            if transaction.amount > 1000 or self.leftTimeViolation(sorted_transactions, i) or self.rightTimeViolation(sorted_transactions, i):
                invalid_transactions.append(transaction.detail)
        
        return invalid_transactions