import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-28&sortBy=publishedAt&apiKey=90820dd742d746429289ae2a4acf46b2"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------------------------------------------")