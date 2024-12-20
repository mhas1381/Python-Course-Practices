from bs4 import BeautifulSoup
import requests
import lxml
endpoint = 'https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

web_page = requests.get(url = endpoint , headers=header)

soup = BeautifulSoup(web_page.content , 'html.parser')
price = soup.find(class_ = "a-offscreen").get_text()
print(price)
