import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt6751668/"

headers = {'User-Agent': 'Mozilla/5.0'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_desc = soup.select_one('meta[property="og:description"]')

image = og_image['content'] if og_image else ""
title = og_title['content'] if og_title else ""
desc = og_desc['content'] if og_desc else ""

print(image)
print(title)
print(desc)
#Nama : Safina Zalfalia Putri
#No Absen : 25
#Kelas : XI TKJ 4