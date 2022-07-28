from termcolor import colored
from service.service_input import ServiceInput
from service.transaction import Transactions
from service.people import People
from service.payment import Payments

SEPARATER=colored("=================", 'yellow')

def app(service_input: ServiceInput):
    print("\n{separater}Step 1: Transaction List{separater}".format(separater=SEPARATER))
    transactions = Transactions(service_input.value)
    transactions.print()
    
    print("\n{separater}Step 2: Group transaction by lender-borrower pair{separater}".format(separater=SEPARATER))
    people = People(transactions)
    people.print_all_lending()
    
    print("\n{separater}Step 3: Reduce bidirectional transaction into unidirectional{separater}".format(separater=SEPARATER))
    people.reduce_bidirectional_transaction()
    people.print_all_lending()
    
    print("\n{separater}Step 4: Calculate Net Flow per Person{separater}".format(separater=SEPARATER))
    people.calculate_receivable()
    people.calculate_payable()
    people.calculate_net_flow()
    people.print_final_result()
    
    print("\n{separater}Step 5: Payments (Borrower, Amount, Lender) {separater}".format(separater=SEPARATER))
    payments = Payments(people)
    print(payments.value)
    
    return payments