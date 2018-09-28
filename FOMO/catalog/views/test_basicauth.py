import requests


response = requests.get('http://localhost/catalog/productsearch', auth=('test@test.com', 'TestTest1'), params={
    'page':2,
    'category': 'Exotic',
    'product': 'a',
    'max_price': 1200.00,

})

print('Status code', response.status_code)
print(response)
print(response.json())
