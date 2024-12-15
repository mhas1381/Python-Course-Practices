import requests
from bs4 import BeautifulSoup

web_page = requests.get(url = 'https://news.ycombinator.com/')

soup = BeautifulSoup(web_page.text , 'html.parser')

articles = soup.find_all(class_ = "titleline")

articles_text = []
articles_link = []
for article in articles:
    text = article.get_text()
    articles_text.append(text)
    link = article.find('a')['href']
    articles_link.append(link)

article_upvote = [int(score.text.split()[0]) for score in soup.find_all(class_ = "score")]

# print(articles_text)
# print(articles_link)
# print(article_upvote)
highest_upvote = article_upvote.index(max(article_upvote))
print(articles_text[highest_upvote])
print(articles_link[highest_upvote])
print(max(article_upvote))
