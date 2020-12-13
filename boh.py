'''Back of House.'''

import json

# inventory used for initial setup
'''inventory = {
    'protein': {
        'pork': 150,
        'chicken': 250,
        'shrimp': 100,
        },

    'side': {
        'rice': 500,
        'salad': 200,
        },

    'pickle': {
        'kimchi': 400,
        'atchara': 400,
        },

    'add_ons': {
        'egg': 200,
        },

    'misc': {
        'seasoning': 500,
        },

    }'''

# Load the inventory. If the file is missing, uncomment to create file and dump
# contents.
filename = 'inventory.json'
try:
    with open(filename) as f:
        inventory = json.load(f)
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
    # for initial setup
    '''with open(filename, 'w') as f:
        json.dump(inventory, f)'''
else:
    # read inventory successfully
    pass

def display_menu(inventory):
    """Display menu items from the current inventory."""
    print(f"Step One, pick your protein:")
    print('{:-^30}'.format(''))
    for protein in inventory['protein'].keys():
        print(f"{protein.title():>8}", end=" ")

    print(f"\n\nStep Two, choose your side:")
    print('{:-^30}'.format(''))
    for side in inventory['side'].keys():
        print(f"{side.title():>8}", end=" ")

    print(f"\n\nStep Three, choose your pickle:")
    print('{:-^30}'.format(''))
    for pickle in inventory['pickle'].keys():
        print(f"{pickle.title():>8}", end=" ")

    print(f"\n\nStep Four, get an add-on (Optional):")
    print('{:-^30}'.format(''))
    for add_ons in inventory['add_ons'].keys():
        print(f"{add_ons.title():>8}", end=" ")


def make_order(inventory):
    """Make an order and check the inventory."""
    print("\n\nOrder ->")
    active = True

    while active:
        protein = input("Protein Option: ")
        protein = protein.lower()
        if protein in inventory['protein'].keys():
            current_stock = inventory['protein'].get(protein)
            inventory['protein'][protein] = current_stock - 1
            break
        else:
            print("Invalid input.")

    while active:
        side = input("Side Option: ")
        side = side.lower()
        if side in inventory['side'].keys():
            current_stock = inventory['side'].get(side)
            inventory['side'][side] = current_stock - 1
            break
        else:
            print("Invalid input.")

    while active:
        pickle = input("Pickle Option: ")
        pickle = pickle.lower()
        if pickle in inventory['pickle'].keys():
            current_stock = inventory['pickle'].get(pickle)
            inventory['pickle'][pickle] = current_stock - 1
            break
        else:
            print("Invalid input.")

    while active:
        add_ons = input("Add-ons (or None): ")
        add_ons = add_ons.lower()
        if add_ons in inventory['add_ons'].keys():
            current_stock = inventory['add_ons'].get(add_ons)
            inventory['add_ons'][add_ons] = current_stock - 1
            break
        elif add_ons == 'none':
            break
        else:
            print("Invalid input.")

    order = {
        'protein': protein,
        'side': side,
        'pickle': pickle,
        'add_ons': add_ons,
        }
    return order

