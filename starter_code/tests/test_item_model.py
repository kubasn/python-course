from unittest import TestCase
from models.item import ItemModel

class TestItem(TestCase):
    def test_create_item(self):
        item = ItemModel('test',20.25)
        # third arg - message that will display if test will fail
        self.assertEqual(item.name,'test','The name of item after creation does not equal the constructor argument')
        self.assertEqual(item.price,20.25,'The price of item after creation does not equal the constructor argument')

    def test_item_json(self):
        item = ItemModel('test',20.25)
        expected = {'name':'test','price':20.25}
        self.assertEqual(item.json(),expected,'The JSON export of the item is incorrect.')
        