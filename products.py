import os # operating system

# 读取档案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品, 价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 让使用者输入
def user_input(products):
	while True:
		name = input('Please the name of product: ')
		if name == 'q':
			break
		price = input('Please input the price: ')
		products.append([name, price])
	print(products)
	return products

# 印出所有购买记录
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

# 写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品, 价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 检查档案在不在
		print('yeah! Found it!')
		products = read_file(filename)
	else:
		print('Cannot find the file!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()


# This code is refactor