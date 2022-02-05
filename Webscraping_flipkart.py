import requests
from bs4 import BeautifulSoup
import csv

def total_pages():
    url='https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = requests.get(url)
    bs = BeautifulSoup(response.content, "html.parser")
    search = bs.find('span', attrs={'class':'_10Ermr'})
    l=list(search.text.split(" "))
    print(l)
    pages = int(l[5].replace(",",""))//int(l[3]) + 1
    return pages

print(total_pages())

with open("mobiles.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["NAME", "PRICE", "RATING"])

for i in range(1,4): 
    url='https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    names=[] 
    prices=[] 
    ratings=[]

    for j in soup.findAll('a', href=True, attrs={'class' : '_1fQZEK'}):
        name=j.find('div', attrs={'class' : '_4rR01T'})
        price=j.find('div', attrs={'class' : '_30jeq3 _1_WHN1'})
        rating=j.find('div', attrs={'class' : '_3LWZlK'})
        names.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)

    with open("mobiles.csv", "a") as f:
        csv_writer = csv.writer(f)
        for l in range(len(names)):
            if(float(ratings[l])>=4.4):
                csv_writer.writerow( [names[l], prices[l], ratings[l]] )
    
with open("mobiles.csv", "r") as f:
    csv_reader =csv.reader(f)
    next(csv_reader)
    for k in csv_reader:
        print(k)