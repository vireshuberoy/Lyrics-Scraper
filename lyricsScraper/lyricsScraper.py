import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

url = "http://www.metrolyrics.com/my-mom-lyrics-eminem.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
lyrics = soup.find("div", {"id" : "lyrics-body-text"})
lyrics = str(lyrics)
randomLyrics = re.sub('<[^>]+>', '', lyrics)
# randomLyrics = randomLyrics.trim('\n')
randomLyrics = re.sub(r'(\n\s*)+\n+', '\n\n', randomLyrics)
print(randomLyrics)

with open('lyrics.txt', 'w+') as file:
    file.write(str(randomLyrics))
    print("File Written")
# print(lyrics)