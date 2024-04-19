from bs4 import BeautifulSoup
import requests
import pandas as pd

# fetch the URL and save the HTML in data folder
def fetchAndSaveToFile(url , path):
    r = requests.get(url)
    with open(path , 'w' , encoding='utf-8') as f:
        f.write(r.text)

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# URL of the file

fetchAndSaveToFile(url , 'data/flipkart.html')

data = {'Title': [] , 'Price': []}

with open('data/flipkart.html' , encoding='utf-8') as r:
    soup = BeautifulSoup(r.read() , 'lxml')
    phones = soup.select("div.KzDlHZ")
    prices = soup.find_all('div' , class_="Nx9bqj _4b5DiR")
    #appending the phone names
    for iphone in phones:
        data["Title"].append(iphone.get_text())
    #appending the price
    for price in prices:
        data["Price"].append(price.get_text())


#converting dict to dataframe
df = pd.DataFrame.from_dict(data)

#saving the file    
df.to_csv('files/iphone.csv' , index=False)
df.to_json('files/iphone.json')
