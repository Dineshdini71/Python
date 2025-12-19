from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
UURL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(UURL)
website_text = response.text

soup = BeautifulSoup(website_text, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
with open("movie_title.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")






# for n in range(len(movie_titles) - 1, 0 , -1):
#     names = movie_titles[n]





















































# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_website = response.text
#
# soup = BeautifulSoup(yc_website, 'html.parser')
# article_texts = []
# article_links = []
# article_score = []
# for title in soup.find_all(name='span', class_="titleline"):
#     text = title.getText()
#     article_texts.append(text)
#     article_link = title.select("a")[0]
#     link = article_link.get("href")
#     article_links.append(link)
#     article_score = title.find_all_next(name="span", class_='score')
#     score = article_score
#     article_score.append(score)
#
#
# print(article_texts)
# print(article_links)
# print(article_score)






















# with open("website.html") as fb:
#     content = fb.read()
# soup = BeautifulSoup(content, 'html.parser')
# li_tag = soup.find_all("h1", id="name")
# for tag in li_tag:
#     print(tag)
#
# company_url = soup.select_one("p a")
# print(company_url)