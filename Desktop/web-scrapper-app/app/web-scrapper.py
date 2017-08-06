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

for container in containers:
    brand = container.div.div.a.img["title"]
    brands = []
    brands.append(brand)

    item = container.find_all("a", {"class":"item-title"})
    product_name = item[0].text
    product_names = []
    product_names.append(product_name)

    price = container.find_all("li", {"class":"price-ship"})
    shipping_price = price[0].text.strip()
    shipping_prices = []
    shipping_prices.append(shipping_price)

    print("Brand: "+ brand)
    print("Product name: " + product_name)
    print("Shipping price: " + shipping_price + "\n" + "-----------------------------------")


headers = ["brand", "product_name", "shipping_price"]
df = pd.DataFrame(headers)
df.columns.transverse = [headers]
headers.to_product.xlsx

#
# GRAPHIC DATA WORDCLOUD
#

wc.to_file("product_name.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()

#
# BAR CHART
#

df = pd.DataFrame({'word':['w1','w2','w3'],'freq':[1,2,3})
df.plot.bar()
