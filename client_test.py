import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
      self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
      self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_Bzero(self):
      quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      ]
      """ ------------ Add the assertion below ------------ """
      for q in quotes:
        self.assertEqual(getRatio(q['top_ask']['price'], q['top_bid']['price']), None)
  def test_getRatio_Azero(self):
      quotes = [
        {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 100, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      ]
      """ ------------ Add the assertion below ------------ """
      for q in quotes:
        self.assertEqual(getRatio(q['top_ask']['price'], q['top_bid']['price']), 0)
  def test_getRatio_Bothzero(self):
      quotes = [
        {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      ]
      """ ------------ Add the assertion below ------------ """
      for q in quotes:
        self.assertEqual(getRatio(q['top_ask']['price'], q['top_bid']['price']), None)



if __name__ == '__main__':
    unittest.main()
