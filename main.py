import requests
import pprint
from bs4 import BeautifulSoup


URL="https://www.youtube.com/results?search_query=tool"
page=requests.get(URL).text
soup=BeautifulSoup(page, "lxml")

results=soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")

videos=soup.find_all("div", class_="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix")

videoList=[]

#print(videos[0].prettify())

for a in videos: 
    """ print(a.prettify())
    print("\n") """
    listItems=a.ul.find_all("li", recursive=False)
    thumbnail=a.img.get("data-thumb")
    thumbnail=thumbnail if thumbnail else a.img.get("src")
    duration=a.span.text.strip("\n")
    title=a.h3.a.text
    videoList.append({"uploaded": listItems[0].text, "views": listItems[1].text, "thumbnail": thumbnail, "duration": duration, "title": title})

""" for item in videoList:
    print(item)
    print("\n") """

print(videoList[0])

#print(soup.prettify())