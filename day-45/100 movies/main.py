from bs4 import BeautifulSoup
import requests

web_page = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(web_page.text, 'html.parser')

movies = soup.select("h2 strong")[::-1]

for movie in movies:
    with open('movies.txt', "a") as file:
        file.write(f"{movie.get_text()}\n")
