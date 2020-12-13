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

        order = make_order(inventory, 'pork', 'rice', 'kimchi', 'egg')
        my_order =  {
                'protein': 'pork',
                'side': 'rice',
                'pickle':'kimchi',
                'add_ons': 'egg',
            }
        self.assertEqual(order, my_order)

if __name__=='__main__':
    unittest.main()
