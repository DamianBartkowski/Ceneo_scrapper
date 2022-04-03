import requests
from bs4 import BeautifulSoup


url = "https://www.ceneo.pl/95365253#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select('div.js_product-review')
review = reviews.pop()
 
print(type(reviews))
print(type(page_dom))
print(type(review))

review_id =review["data-entry-id"]
print(review_id)


author =review.select("span.user-post__author-name").pop(0).text.strip()
print(type(author))
print(author)

recommendation = review.select("span.user-post__author-recomendation > em").pop(0).text
print(recommendation)
recommendation == True if recommendation == "polecam" else False if recommendation == "Nie polecam" else None
stars = review.select("span.user-post__score-count").pop(0).text
stars = float(stars.split("n").pop(0).replace(",","."))
print(type(stars))
print(stars)

concent = review.select("div.user-post__text").pop(0).string
concent.replace("\n"," ")
print(type(concent))
print(concent)

publish_date = review.select("span.user-post__published > time:nth-child(1)").pop("datetime")
