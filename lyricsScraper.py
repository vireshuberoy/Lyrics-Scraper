import requests
import urllib.request
from bs4 import BeautifulSoup
import re

songName = input("Enter the song name: ")
songName = songName.split(' ')
# print(songName)

artistName = input("Enter the artist name: ")
artistName = artistName.split(' ')
# print(artistName)

songNameStr = songName[0]
for i in range(len(songName)):
    try:
        songNameStr = songNameStr + '-' + songName[i + 1]
    except:
        pass

artistNameStr = artistName[0]
for i in range(len(artistName)):
    try:
        artistNameStr = artistNameStr + '-' + artistName[i + 1]
    except:
        pass

songNameStr = str(songNameStr)
artistNameStr = str(artistNameStr)

# print(songNameStr)
# print(artistNameStr)

url = "http://www.metrolyrics.com/" + songNameStr + '-' + "lyrics" + '-' + artistNameStr + ".html"
print("url is: ", url)
response = requests.get(url)
if response.status_code == 200:
    pass
else:
    print('Please check if you have entered the correct spelling of the song\'s and/or the artist\'s name ')
    exit()


soup = BeautifulSoup(response.text, "html.parser")
lyrics = soup.find("div", {"id" : "lyrics-body-text"})
lyrics = str(lyrics)
randomLyrics = re.sub('<[^>]+>', '', lyrics)
randomLyrics = re.sub(r'(\n\s*)+\n+', '\n\n', randomLyrics)
print(randomLyrics)

with open('lyrics.txt', 'w+') as file:
    file.write(str(randomLyrics))
    print("File Written")
