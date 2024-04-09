import requests
from bs4 import BeautifulSoup

url = 'https://plataforma.institutodelmilagro.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('title').text

print(title)