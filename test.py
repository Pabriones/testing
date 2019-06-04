import unittest
from menuitem import MenuItem
from payment import Payment
from menu import Menu
from ordertotal import OrderTotal
from inventory import Inventory


class MenuItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1.50,'item1',1)

    def test_string(self):
        self.assertEqual(str(self.item),self.item.itemname)
    
    def test_GetItemNumber(self):
        self.assertEqual(self.item.getItemPrice(),1.50)

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.menuitem=MenuItem(1,'item1', 1.50)
        self.orderitem=OrderItem(self.item,1)
    def test_Quantity(self):
        self.assertEqual(self.menuitem.getQuantity(),2)
    def test_item(self):
        item=self.orderitem.getItem()
        self.assertEqual(str(item),'item1')


class orderTotalTest(unittest.TestCase):
    def test_CalculateTotal(self):
        Payment=self.OrderTotal.calcTotal()
        self.assertEqual(str(Payment),'Your total payment is ' + Payment)