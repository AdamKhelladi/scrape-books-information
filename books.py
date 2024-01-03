
# Scrape Books Information

import requests
from bs4 import BeautifulSoup as bs

url = "https://books.toscrape.com/"
req = requests.get(url).text

soup = bs(req, "lxml")

website_name = soup.find("div", {"class": "col-sm-8 h1"}).text
# print(website_name)

books = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
# print(len(books))

for book in books: 
  book_title = book.find("h3").text
  # print(book_title)

  book_price = book.find("p", {"class": "price_color"}).text
  # print(book_price)

  book_info = {
    "Book Title": book_title,
    "Book Price": book_price
  }

  print(book_info)
  print("-----------------------")