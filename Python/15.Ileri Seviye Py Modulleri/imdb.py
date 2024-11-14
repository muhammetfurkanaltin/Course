import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent":  "User-Agent"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li", limit = 10)

for item in liste : 
    filmadi = item.find("h3", {"class":"ipc-title__text"}).text
    puan = item.find("span", {"class": "ipc-rating-star"}).text
    print(filmadi,puan)