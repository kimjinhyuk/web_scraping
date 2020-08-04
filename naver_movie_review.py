import requests
from bs4 import BeautifulSoup
import csv

url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_select = soup.select('div[id=content] ul[class=lst_detail_t1] > li > dl[class=lst_dsc]')

movie_data_list = []
for movie in movie_select:
    a_tag = movie.select_one('dl[class=lst_dsc] > dt[class=tit] > a')
    movie_title = a_tag.get_text()
    movie_link = a_tag['href'].split('?code=')[1]
    movie_data = {
        'title' : movie_title,
        'link' : movie_link
    }
    movie_data_list.append(movie_data)




