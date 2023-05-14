import requests
from bs4 import BeautifulSoup as bs

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = bs(content, 'lxml')
    courses_html_tags = soup.find_all_previous('h5')
