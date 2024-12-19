from bs4 import BeautifulSoup
import requests
import lxml
endpoint = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

web_page = requests.get(url = endpoint , headers=header)
print(web_page.status_code)

soup = BeautifulSoup(web_page.content , 'html.parser')
price = soup.find(class_ = "a-offscreen").get_text()
print(price)
