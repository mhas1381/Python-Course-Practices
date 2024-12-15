from bs4 import BeautifulSoup
import requests

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
web_page = requests.get(url =f"https://www.billboard.com/charts/hot-100/{user_date}" , headers=headers)

soup = BeautifulSoup(web_page.text , 'html.parser')

data = soup.find_all(name = 'h3' , class_ = 'a-truncate-ellipsis')

movies = [movie.get_text().strip() for movie in data]

CLIENT_ID = '742ae9877b6d4617baa9db941169b3f6'
CLIENT_SECRET = 'c8e9a23cff7d4e3eb1c609129970ee2e'



