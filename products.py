# 检查文件在不在
import os # operating system

# 读取档案
products = []
if os.path.isfile('products.csv'): # 检查档案在不在
	print('yeah! Found it!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品, 价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
	print(products)
else:
	print('Cannot find the file....')

# 让使用者输入
while True:
	name = input('Please the name of product: ')
	if name == 'q':
		break
	price = input('Please input the price: ')
	products.append([name, price])
print(products)

# 印出所有购买记录
for p in products:
	print('The price of', p[0], 'is', p[1])

# 写入档案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')