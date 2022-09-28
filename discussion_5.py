import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		maxi = 0
		maxitem = None
		for a in self.items:
			if a.stock > maxi:
				maxi = a.stock
				maxitem = a
		return maxitem


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		maxi = 0
		maxitem = None
		for a in self.items:
			if a.price > maxi:
				maxi = a.price
				maxitem = a
		return maxitem




# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		a = "aaaa"
		b = "bbbb"
		c = "ccab"
		d = ""
		self.assertEqual(count_a(a), 4, "Testing count_a to equal 4")
		self.assertEqual(count_a(b), 0, "Testing count_a to equal 0")
		self.assertEqual(count_a(c), 1, "Testing count_a to equal 1")
		self.assertEqual(count_a(d), 0, "Testing count_a with empty string")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		wh1 = Warehouse()
		self.assertEqual(len(wh1.items), 0, "Testing that string begins empty (len of 0)")
		wh1.add_item(self.item1)
		self.assertEqual(len(wh1.items), 1, "Testing that add_item works for expected len 1")



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		wh2 = Warehouse([self.item1, self.item2, self.item3])
		wh3 = Warehouse()
		self.assertEqual(wh2.get_max_stock().name, "Water", "Testing that maximum item returns a name of 'Water'")
		self.assertEqual(wh3.get_max_stock(), None, "Determining if an empty items list returns None")
		self.assertEqual(wh2.get_max_stock().stock, 100, "Checking if max item name and max stock quantity match")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		wh4 = Warehouse([self.item1, self.item2, self.item3])
		wh5 = Warehouse()
		self.assertEqual(wh4.get_max_price().name, "Beer", "Testing that max priced item matches name 'Beer'")
		self.assertEqual(wh5.get_max_price(), None, "Testing that empty items list returns None (as there is no max price)")
		self.assertEqual(wh4.get_max_price().price, 6, "Checking that highest priced item, Beer, has expected price of 6")

def main():
	unittest.main()

if __name__ == "__main__":
	main()