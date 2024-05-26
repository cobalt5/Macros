import requests
from bs4 import BeautifulSoup

response = requests.get("https://scrapeme.live/shop/")
soup = BeautifulSoup(response.text, 'lxml')

print(soup.prettify())

# description = soup.find('li', class_='post-732 product type-product status-publish has-post-thumbnail product_cat-flame product_cat-pokemon product_tag-blaze product_tag-charmeleon product_tag-flame first instock taxable shipping-taxable purchasable product-type-simple').text
# print(description)

# products = soup.find('ul', class_='products columns-4')

products = soup.findAll('h2', class_="woocommerce-loop-product__title")
for product in products:
    print(product.text)



