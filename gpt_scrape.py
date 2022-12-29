import requests
from bs4 import BeautifulSoup

url = 'https://subslikescript.com/movies'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
script_list = soup.find('ul', {'class': 'scripts-list'})

for link in script_list.find_all('a'):
  print(link.text)