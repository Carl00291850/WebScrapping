import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=20&N=600000022%20600000280%2050001312%2050001314%2050001315%2050001944')
soup = BeautifulSoup(page.content, 'html.parser')
containers = soup.find_all('div',class_='item-container')

for container in containers:
    brand_container = container.find('a',class_='item-brand')
    brand_title = brand_container.img["title"]

    Product_container = container.find_all('a' ,class_='item-title')
    Product_name = Product_container[0].text

    Shipping_container = container.find_all('li',class_='price-ship')
    Shipping_name = Shipping_container[0].text.strip()

    Price_container = container.find_all('li',class_='price-current')
    price_name = Price_container[0].text.strip('|\n')



    print(brand_title)
    print(Product_name)
    print(Shipping_name)
    print(price_name)
