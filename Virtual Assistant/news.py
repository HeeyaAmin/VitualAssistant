import requests
import json
main_url = 'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6ba067a9f58d4dae8814f3f91cedcec2'
nws = requests.get(main_url).json()
article = nws["articles"]
nws_article=[]
for arti in article:
    nws_article.append(arti['title'])
    for i in range(len(nws_article)):
        print(nws_article[i])
