import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('movie.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year', 'Rating'])
page = 1
url = f'https://geo.saitebi.ge/main/new/{page}'

while page < 6:
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')

    block = soup.find('div', id='content')
    all_movies = block.find_all('div', class_='movie-items-wraper')

    for each in all_movies:
        title = each.find('div', class_='hover-wraper').find('div', class_='h-title-origin').text
        year = each.find('div', class_='hover-wraper').find('div', class_='h-year').text
        imdb = each.imdb.text
        file_obj.writerow([title, year, imdb])

    sleep(randint(15,20))

    page += 1
file.close()