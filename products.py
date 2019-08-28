products = []
while True:
	name = input('Please the name of product: ')
	if name == 'q':
		break
	price = input('Please input the price: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)


products[0][0] # products 清单中第0个清单中的第0个