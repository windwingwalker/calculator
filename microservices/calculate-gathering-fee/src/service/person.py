from typing import Dict, List
from termcolor import colored
from typing import NewType
import json

RECEIVABLE=colored("receivable", "blue")
PAYABLE=colored("payable", "red")
NET_FLOW=colored("net flow", "green")

Name = NewType('Name', str)

class Person:
    def __init__(self, name: Name) -> None:
        self.name: Name = name
        self.lend: Dict[Name, float] = {} # store sth like {"A": 30, "B": 20}, which means the self lend $30 to A and $20 to B
        self.borrow: Dict[Name, float] = {}
        self.receivable: float = 0.0 # the sum of money the self lending to others
        self.payable: float = 0.0 # the sum of money the self borrowing from others
        self.net_flow: float = 0.0 # receivable - payable
        
    def is_lending_to(self, borrower_name: Name) -> bool:
        # Return true if a person(borrower_name) is within self.lend
        return borrower_name in self.lend

    def is_borrowed_from(self, lender_name: Name) -> bool:
        return lender_name in self.borrow
    
    def get_borrower_name_list(self) -> List[Name]:
        return [name for name in self.lend]

    def print_lending(self) -> None:
        print('{name}\'s lending includes: {lend}'.format(name=self.name, lend=json.dumps(self.lend)))
        
    def get_expression(self, type: str) -> str:
        expression = ""
        foo = self.lend if type == "receivable" else self.borrow
        for i in foo:
            expression += str(foo[i]) + "(" + i + ")"
            expression += " + "
        expression = expression[:-3]
        if len(expression) != 0:
            expression += " = "
        return expression

    def print_receivable(self) -> None:
        print('{name}\'s {receivable_str} is: {receivable_expression}{receivable}'.format(
            name=self.name, 
            receivable=colored(self.receivable, "blue"), 
            receivable_expression=self.get_expression("receivable"), 
            receivable_str=RECEIVABLE))

    def print_payable(self) -> None: 
        print('{name}\'s {payable_str} is: {payable_expression}{payable}'.format(
            name=self.name, 
            payable=colored(self.payable, "red"), 
            payable_expression=self.get_expression("payable"), 
            payable_str=PAYABLE))

    def print_net_flow(self) -> None:
        print('{name}\'s {net_flow_str} is: {receivable} - {payable} = {net_flow}'.format(
            name=self.name, 
            net_flow_str=NET_FLOW, 
            receivable=colored(self.receivable, "blue"), 
            payable=colored(self.payable, "red"), 
            net_flow=colored(self.net_flow, "green")))
     