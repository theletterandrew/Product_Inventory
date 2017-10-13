class Product(object):
	def __init__(self, name, idNum, quantity, price, description):
		self.name = name
		self.idNum = idNum
		self.quantity = quantity
		self.price = price
		self.description = description

	def getName(self):
		return self.name

	def getIdNum(self):
		return self.idNum

	def getQuantity(self):
		return self.quantity

	def getPrice(self):
		return self.price

	def getDescription(self):
		return self.description

	def getValue(self):
		return self.price * self.quantity

	def __str__(self):
		return "Name: %s \nID: %s \nQuantity: %s \nPrice: %s \nDescription: %s \nTotal Value in inventory: $%.2f" % (self.name, self.idNum, self.quantity, self.price, self.description, self.getValue())


# wallet1 = Product("Black Wallet", 1, 20, 19.99, "Black pvc wallet with studs.")
# belt1 = Product("Brown Belt", 2, 10, 30, "A pleather brown belt.")

# print(wallet1)
# print(belt1)

name = input("Enter a product name: ")
productID = int(input("Enter a product ID: "))
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
description = input("Enter a description of the product: ")

product = Product(name, productID, quantity, price, description)

print(product)