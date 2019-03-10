products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		print('結束')
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = [name, price]
	products.append(p)
# print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:
	f.write('商品名稱, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')





