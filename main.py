# for currency formatting.
import locale

locale.setlocale(locale.LC_ALL, '')

# inventory for now
inventory = {
        'pork': 150,
        'chicken': 250,
        'shrimp': 100,
        'seasoning': 500,
        'rice': 500,
        'salad': 200,
        'kimchi': 400,
        'atchara': 400,
        'egg': 200,
        }

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

def make_order(inventory):
    """Make an order and check the inventory."""
    protein = input("Step One: Pork, Chicken, Shrimp\n\tOption: ")
    if protein in inventory.keys():
        current_stock = inventory.get(protein)
        inventory[protein] = current_stock - 1
    else:
        # add a flag to loop for valid input
        pass
    side = input("Step Two: Rice, Salad\n\tOption: ")
    pickle = input("Step Three: Kimchi, Atchara\n\tOption: ")
    add_ons = input("Step Four: Egg, None\n\tOptions: ")
    order = {
        'protein': protein,
        'side': side,
        'pickle': pickle,
        'add_ons': add_ons,
        }
    return order


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

# main program begins here.
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
