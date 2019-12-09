#import libraies for wen scrapping
import requests
from bs4 import BeautifulSoup
#request the data form the website
page = requests.get('https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=20&N=600000022%20600000280%2050001312%2050001314%2050001315%2050001944')
#load data to  bs4 and put it into a variable where beutufullsoup can understand
soup = BeautifulSoup(page.content, 'html.parser')
#get the first item of the web page to start webscrapping
containers = soup.find_all('div',class_='item-container')
#make a for loop of the first item to grab  the remaining item to get
for container in containers:
    brand_container = container.find('a',class_='item-brand')
    brand_title = brand_container.img["title"]

    Product_container = container.find_all('a' ,class_='item-title')
    Product_name = Product_container[0].text

    Shipping_container = container.find_all('li',class_='price-ship')
    Shipping_name = Shipping_container[0].text.strip()

    Price_container = container.find_all('li',class_='price-current')
    price_name = Price_container[0].text.strip('|\n\s')

#print the items of thr wen page
    print(brand_title)
    print(Product_name)
    print(Shipping_name)
    print(price_name)
