'''Accounting'''

import locale

# for currency formatting, set currency settings
locale.setlocale(locale.LC_ALL, '')

def get_check_num():
    """Returns the check number for the customer."""
    check_count = 0 # use a file reader, for now temp.

    return check_count + 1


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
    customer.check_num = get_check_num()
    print(f"Table: {customer.table_assigned}\tChk: #{customer.check_num:04d}")
    print(f"Your total amount is: {locale.currency(total, grouping=True)}")
    # add code later for payment options: cash, credit/debit card, mobile
