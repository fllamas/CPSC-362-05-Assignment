'''Front of House.'''

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

    def __init__(self, table_assigned, order, check_num=0):
        """Initialize attributes to describe a customer."""
        self.table_assigned = table_assigned
        self.order = order
        self.check_num = check_num
