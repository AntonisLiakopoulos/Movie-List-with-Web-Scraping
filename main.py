from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = soup.find_all(name="h3",class_="title")

try:
    with open("movie_list.txt", "r", encoding="utf-8"):
        pass
except FileNotFoundError:
    with open("movie_list.txt", "a", encoding="utf-8") as data:
        for movie in reversed(movies):
            with open("movie_list.txt", "a", encoding="utf-8") as data:
                data.write(movie.getText() + "\n")



