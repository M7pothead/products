products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		print('結束')
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = [name, price]
	products.append(p)
print (products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('prodicts.csv', 'w', encoding='utf-8')as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #加法只能用於字串加字串，若型別是int會變數字加法



