total_number = int(input('Enter the total number of books'))
products = []
if total_number < 1:
    print('Invalid number')
    exit()
# loop
for x in range(total_number):
    product_name = input(f"Enter product {x +1} name")
    product_qty = input(f"Enter product {product_name} quantity")
    product_price = input(f"Enter product {product_name} price")
    product = {
        'name': product_name,
        'quantity': product_qty,
        'price': product_price
    }
    products.append(product)
    if x == total_number-1:
        print(products)
search = input('Enter a name to search')


def search_product(name):
    product_dicts = [ele for ele in products if ele['name'] == name]
    if len(product_dicts):
        print(product_dicts[0])
        return product_dicts[0]
    else:
        print('No products with this name')


search_product(search)
