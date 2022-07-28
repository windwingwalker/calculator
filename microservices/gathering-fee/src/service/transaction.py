from typing import NewType, List

Name = NewType('Name', str)

class Transaction(object):
    def __init__(self, lender_name: str, amount: float, borrower_name: str) -> None:
        self.lender_name: Name = lender_name
        self.borrower_name: Name = borrower_name
        self.amount: float = amount
    
    @property
    def lender_name(self):
        return self._lender_name
    
    @lender_name.setter
    def lender_name(self, value):
        if not isinstance(value, str):
            raise TypeError("The type of lender name is not str")
        self._lender_name = Name(value)
        
    @property
    def borrower_name(self):
        return self._borrower_name
    
    @borrower_name.setter
    def borrower_name(self, value):
        if not isinstance(value, str):
            raise TypeError("The type of borrower name is not str")
        self._borrower_name = Name(value)
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("The type of amount is not number")
        self._amount = value
    
    def print(self) -> None:
        print([self.lender_name, self.amount, self.borrower_name], end = '')
    
class Transactions:
    def __init__(self, raw_transactions) -> None:
        self.val: List[Transaction] = [Transaction(transaction[0], transaction[1], transaction[2]) for transaction in raw_transactions]
    
    def print(self) -> None:
        for transaction in self.val:
            transaction.print()
        print()