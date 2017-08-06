# WEB SCRAPER

import datetime
import requests
from bs4 import BeautifulSoup #note that the import package command is bs4
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# ISSUE REQUEST

r = requests.get("https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709")

# PARSE RESPONSE

raw = r.text
soup = BeautifulSoup(raw, "html.parser")

# FINDING PRODUCTS

containers = soup.find_all("div", {"class":"item-container"})

print("-----------------------------------" + "\n" + "Search Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("\n" + "-----------------------------------")
print("FINDING GRAPHIC CARDS @newegg.com")
print("-----------------------------------")
print("Welcome @amazonwong! *(^_^)* " + "\n" + "================================")
print("THERE ARE " + str(len(containers)) + " PRODUCTS:" + "\n" + "================================")

brands = []
product_names = []
shipping_prices = []

for container in containers:
    brand = container.div.div.a.img["title"]
    brands.append(brand)

    item = container.find_all("a", {"class":"item-title"})
    product_name = item[0].text
    product_names.append(product_name)

    price = container.find_all("li", {"class":"price-ship"})
    shipping_price = price[0].text.strip()
    shipping_prices.append(shipping_price)

    print("Brand: " + brand)
    print("Product name: " + product_name)
    print("Shipping price: " + shipping_price + "\n" + "-----------------------------------")


database = [brands, product_names, shipping_prices]
headers = ["Brand", "Product Name", "Shipping Price"]

df = pd.DataFrame(database).transpose()
df.columns = headers
df.to_csv("data/graphic_cards.csv")

#
# GRAPHIC DATA WORDCLOUD
#


wordcloud = WordCloud().generate('data/graphic_cards.csv'.join(product_names))
plt.figure()
plt.axis("off")
plt.imshow(wordcloud)
plt.show()
plt.savefig("data/wordcloud.png")

#
# BAR CHART
#

df['brands'].value_counts().plot(kind='bar')
plt.show()
plt.savefig("data/barchart.png")
