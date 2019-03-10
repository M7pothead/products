#有個風險是一開始就打開檔案，若無偵測到檔案會crash
#所以讀取檔案相關的程式應要加入檢查檔案的功能
import os #operation system
if os.path.isfile('products.csv'):
	print('yeah 找到檔案')
else:
	print('找無檔案')


#讀取
products = []
with open('products.csv', 'r')as f:
	for line in f:
		if '商品名稱, 價格' in line:
			continue #跳到下一行
		name, price = line.strip().split(',')
		products.append([name, price])
		
print(products)


#使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品名稱, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')





