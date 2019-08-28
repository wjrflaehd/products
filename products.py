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

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')