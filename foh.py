'''Front of House.'''

# for currency formatting.
import locale

from boh import make_order

# set currency settings
locale.setlocale(locale.LC_ALL, '')

# temporary dictionaries for creating tables
table_1 = {
        'id': 'table_1',
        'available': True,
        'min_size': 2,
        'max_size': 5,
        }

table_2 = {
        'id': 'table_2',
        'available': True,
        'min_size': 1,
        'max_size': 2,
        }

table_3 = {
        'id': 'table_3',
        'available': True,
        'min_size': 2,
        'max_size': 4,
        }

tables = [table_1, table_2, table_3]

def manage_table(tables):
    """Manage table availability and size."""
    party_size = input("How many are in your party? ")
    party_size = int(party_size)
    for table in tables:
        if party_size >= table['min_size'] and party_size <= table['max_size']:
            table['available'] = False
            print(f"Now seating you at your table, {table['id']}.")
            return table['id']

    # couldn't find a table after looping through all available tables.
    print("Sorry, there are no available tables right now. Please wait.")
    return None


class Customer:
    """A simple attempt to represent a customer."""

    def __init__(self, table_assigned, order):
        """Initialize attributes to describe a customer."""
        self.table_assigned = table_assigned
        self.order = order


def total_order(order):
    """Add up all the items for an order and return total amount."""
    total = 0
    if order['protein'] == 'pork' or order['protein'] == 'chicken':
        total += 9
    elif order['protein'] == 'shrimp':
        total += 11
    else:
        pass

    if order['add_ons'] == 'egg':
        total += 1
    else:
        pass

    return total


def process_payment(customer):
    """Process payment for customer order(s)."""
    total = total_order(customer.order)
    print(f"Your total amount is: {locale.currency(total, grouping=True)}")
    # add code later for payment options: cash, credit/debit card, mobile

