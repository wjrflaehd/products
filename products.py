products = []
while True:
	name = input('Please the name of product: ')
	if name == 'q':
		break
	price = input('Please input the price: ')
	products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])