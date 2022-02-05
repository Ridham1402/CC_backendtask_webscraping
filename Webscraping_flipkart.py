import requests
from bs4 import BeautifulSoup
import csv


def total_pages():  # return number of pages with different mobiles
    url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = requests.get(url)
    bs = BeautifulSoup(response.content, "html.parser")
    search = bs.find('span', attrs={'class': '_10Ermr'})
    l = list(search.text.split(" "))
    pages = int(l[5].replace(",", ""))//int(l[3]) + 1
    return pages


print(total_pages())

with open("mobiles.csv", "w", encoding="utf-8") as f:  # for writing header to CSV file
    writer = csv.writer(f)
    writer.writerow(["NAME", "PRICE", "RATING"])

for i in range(1, 4):  # iterating for first 3 pages
    url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + \
        str(i)  # taking urls of pages while iterating
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    names = []
    prices = []
    ratings = []

    # iterating for all mobiles on the page
    for j in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
        name = j.find('div', attrs={'class': '_4rR01T'})
        price = j.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        rating = j.find('div', attrs={'class': '_3LWZlK'})
        names.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)

    # for writing mobiles having rating more than or equal to 4.4
    with open("mobiles.csv", "a", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        for l in range(len(names)):
            if(float(ratings[l]) >= 4.4):
                csv_writer.writerow([names[l], prices[l], ratings[l]])

with open("mobiles.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for k in csv_reader:
        print(k)  # printing all products in CSV file