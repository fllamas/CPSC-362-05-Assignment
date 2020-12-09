'''Back of House.'''

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

def make_order(inventory):
    """Make an order and check the inventory."""

    protein = input("Step One: Pork, Chicken, Shrimp\n\tOption: ")
    protein = protein.lower()
    if protein in inventory.keys():
        current_stock = inventory.get(protein)
        inventory[protein] = current_stock - 1
    else:
        # add a flag to loop for valid input
        pass

    side = input("Step Two: Rice, Salad\n\tOption: ")
    side = side.lower()
    if side in inventory.keys():
        current_stock = inventory.get(side)
        inventory[side] = current_stock - 1
    else:
        # add a flag to loop for valid input
        pass

    pickle = input("Step Three: Kimchi, Atchara\n\tOption: ")
    pickle = pickle.lower()
    if pickle in inventory.keys():
        current_stock = inventory.get(pickle)
        inventory[pickle] = current_stock - 1
    else:
        # add a flag to loop for valid input
        pass

    add_ons = input("Step Four: Egg, None\n\tOptions: ")
    add_ons = add_ons.lower()
    if add_ons in inventory.keys():
        current_stock = inventory.get(add_ons)
        inventory[add_ons] = current_stock - 1
    else:
        # add a flag to loop for valid input
        pass

    order = {
        'protein': protein,
        'side': side,
        'pickle': pickle,
        'add_ons': add_ons,
        }
    return order

