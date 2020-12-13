import unittest
import json
from boh import make_order

class OrderTestCase(unittest.TestCase):
    """Tests for 'boh.py'."""

    def test_inventory(self):
        """What happens when you order until stock runs out (i.e. past 0)?"""

        filename = 'inventory.json'
        try:
            with open(filename) as f:
                inventory = json.load(f)
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")
        else:
            # read inventory successfully
            pass

        orders = []
        count = 0
        while count <= 151:
            order = make_order(inventory, 'pork', 'rice', 'kimchi', 'egg')
            orders.append(order)
            count += 1

        my_order =  {
                'protein': 'pork',
                'side': 'rice',
                'pickle':'kimchi',
                'add_ons': 'egg',
            }
        self.assertEqual(orders[0], my_order)

if __name__=='__main__':
    unittest.main()
