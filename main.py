import requests
import pprint
from bs4 import BeautifulSoup

""" def getVideos(search)
    URL="https://www.youtube.com/results?search_query="+search
    page=requests.get(URL)

    print(page.content) """

URL="https://www.youtube.com/results?search_query=tool"
page=requests.get(URL).text
soup=BeautifulSoup(page, "lxml")

results=soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")

for a in results: 
    print(a)
    print("\n")

##print(soup.prettify())