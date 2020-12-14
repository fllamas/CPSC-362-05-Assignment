'''Main program.'''

from foh import *
from boh import *
from accounting import *

#print(f"Before ordering: {inventory}\n")
display_menu(inventory)

def validate_answer():
    """Validate answer in terms of yes/no and returns appropriate string."""

    valid = False
    while valid == False:
        answer = input("\nWould you like add another order? (yes/no): ")
        answer = answer.lower()
        if answer == 'no':
            break
        elif answer == 'yes':
            print("For your next order:", end=" ")
            break
        else:
            # invalid input
            print("Invalid input!")

    return answer


# Empty list to hold multiple orders per customer.
orders = []

active = True
while active:
    order = make_order(inventory)
    orders.append(order)

    answer = validate_answer()
    if answer == 'no':
        break

#print(f"\nMy order: {order}")
#print(f"\nAfter ordering: {inventory}")

#print(f"\nTable availability before: {tables}\n")
print()
table_assigned = manage_table(tables)
#print(f"Your table is: {table_assigned}.")
#print(f"\nAfter assigning table: {tables}\n")

# create a list of customer objects. Holds current processing tickets/orders.
# current_tickets = []
print()
customer_1 = Customer(table_assigned, orders)
process_payment(customer_1)
