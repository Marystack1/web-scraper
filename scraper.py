import requests
from bs4 import BeautifulSoup
import csv

#The URL we want to scrape
url = "http://quotes.toscrape.com"

#1. send an HTTP request to the url
response = requests.get(url)

#check if the requests was successful
if response.status_code == 200:
#parse the HTML content
    print("success! I found the page.")
    soup = BeautifulSoup(response.text, 'html.parser' )

#find the quote containers (they are <div> tags with class 'quote')
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    #Extract the text of the quote
    text = quote.find('span', class_='text').get_text()

    #Extract the author's name 
    author = quote.find('small',class_='author').get_text()

    print (f"Quote:{text}")
    print(f"By:{author}\n" + "_"*20)

else:
        print(f"Failed to retrieve the page. Status code:{response.status_code}")