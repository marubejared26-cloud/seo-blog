import requests
from bs4 import BeautifulSoup

url = "https://example-shop.com/product"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# This looks for the price on the page
price = soup.find("span", {"class": "price"}).text
print(f"The current price is: {price}")

