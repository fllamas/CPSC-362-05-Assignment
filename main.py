'''Main program.'''

from foh import * 
from boh import *

print(f"Before ordering: {inventory}\n")
order = make_order(inventory)
print(f"\nMy order: {order}")
print(f"\nAfter ordering: {inventory}")

print(f"\nTable availability before: {tables}\n")
table_assigned = manage_table(tables)
print(f"Your table is: {table_assigned}.")
print(f"\nAfter assigning table: {tables}\n")

# create a list of customer objects. Holds current processing tickets/orders.
# current_tickets = []

customer_1 = Customer(table_assigned, order)
process_payment(customer_1)
