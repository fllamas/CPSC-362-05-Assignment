'''Accounting'''

import locale
import json

# for currency formatting, set currency settings
locale.setlocale(locale.LC_ALL, '')

def update_check_num(check_count):
    """Update the check number after transaction."""
    check_count += 1

    filename = 'check_number.json'
    try:
        with open(filename, 'w') as f:
            json.dump(check_count, f)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")


def get_check_num():
    """Returns the check number for the customer."""
    filename = 'check_number.json'
    try:
        with open(filename) as f:
            check_count = json.load(f)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

    update_check_num(check_count)

    return check_count


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

    # format customer info before writing transaction to file
    customer_formated = {
            'Table': f"{customer.table_assigned}",
            'Chk': f"#{customer.check_num:04d}",
            'Total amount': f"{locale.currency(total, grouping=True)}",
            'Order': f"{customer.order}",
            }

    # write receipt to file
    filename = 'transaction_history.json'
    try:
        with open(filename, 'a') as f:
            json.dump(customer_formated, f, indent=4)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
