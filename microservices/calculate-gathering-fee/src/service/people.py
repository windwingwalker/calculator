from typing import Dict, NewType
from service.person import Person
from service.transaction import Transactions
import copy

Name = NewType('Name', str)

class People:
    def __init__(self, transactions: Transactions) -> None:          
        self.val: Dict[Name, Person] = self.get_value(transactions)
    
    def get_value(self, transactions: Transactions) -> None:
        res = {}
        for transaction in transactions.val:
            
            if transaction.lender_name not in res:
                res[transaction.lender_name] = Person(transaction.lender_name)
            if transaction.borrower_name not in res:
                res[transaction.borrower_name] = Person(transaction.borrower_name)

            if res[transaction.lender_name].is_lending_to(transaction.borrower_name):
                res[transaction.lender_name].lend[transaction.borrower_name] += transaction.amount
            else:
                res[transaction.lender_name].lend[transaction.borrower_name] = transaction.amount
            
            if res[transaction.borrower_name].is_borrowed_from(transaction.lender_name):
                res[transaction.borrower_name].borrow[transaction.lender_name] += transaction.amount
            else:
                res[transaction.borrower_name].borrow[transaction.lender_name] = transaction.amount
        
        return res
    
    def reduce_bidirectional_transaction(self) -> None:
        res: Dict[Name, Person] = copy.deepcopy(self.val)
        pending_unified_transaction = {}
        for lender in self.val.values():
            for borrower_name in lender.lend: # traverse all borrower of this lender
                if self.val[borrower_name].is_lending_to(lender.name) : # check if lender itself is in borrower's lending list, if so, their transcation can be unified into one transaction
                    if lender.name + "-" + borrower_name not in pending_unified_transaction and borrower_name + "-" + lender.name not in pending_unified_transaction: 
                        pending_unified_transaction[lender.name + "-" + borrower_name] = lender.lend[borrower_name]
        
                    elif borrower_name + "-" + lender.name in pending_unified_transaction:
                        pending_unified_transaction[borrower_name + "-" + lender.name] = pending_unified_transaction[borrower_name + "-" + lender.name] - lender.lend[borrower_name]

        for foo in pending_unified_transaction:
            person1: Name = Name(foo.split("-")[0])
            person2: Name = Name(foo.split("-")[1])
            if pending_unified_transaction[foo] < 0:
                res[person2].lend[person1] = res[person2].lend[person1] - res[person1].lend[person2]
                res[person1].borrow[person2] = res[person1].borrow[person2] - res[person2].borrow[person1]
                del res[person1].lend[person2]
                del res[person2].borrow[person1]
            elif pending_unified_transaction[foo] > 0:
                res[person1].lend[person2] = res[person1].lend[person2] - res[person2].lend[person1]
                res[person2].borrow[person1] = res[person2].borrow[person1] - res[person1].borrow[person2]
                del res[person2].lend[person1]
                del res[person1].borrow[person2]
            else:
                del res[person2].lend[person1]
                del res[person1].lend[person2]
                del res[person2].borrow[person1]
                del res[person1].borrow[person2]

        self.val = res
    
    def calculate_receivable(self) -> None:
        for lender in self.val.values():
            for borrower_name in lender.get_borrower_name_list():
                lender.receivable += lender.lend[borrower_name]
    
    def calculate_payable(self) -> None:
        for lender in self.val.values():
            for borrower_name in lender.get_borrower_name_list(): # traverse all borrower of this lender                
                self.val[borrower_name].payable += lender.lend[borrower_name]

    def calculate_net_flow(self) -> None:
        for person in self.val.values():
            person.net_flow = person.receivable - person.payable

    def print_all_lending(self) -> None:
        for person in self.val.values(): 
            person.print_lending()
    
    def print_final_result(self) -> None:
        for person in self.val.values():
            person.print_receivable()
            person.print_payable()
            person.print_net_flow()
            print("")
            
    def get_net_flow_dict(self) -> dict:
        res = {}
        for person in self.val.values():
            res[person.name] = person.net_flow
        return res