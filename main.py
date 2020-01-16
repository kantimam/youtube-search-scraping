import requests
import pprint
from bs4 import BeautifulSoup


def searchYoutube(query, page=None):
    pageQuery="&page="+str(page) if page else ""
    URL="https://www.youtube.com/results?search_query="+query+pageQuery
    request=requests.get(URL)
    if(request.status_code==200):
        page=request.text
        soup=BeautifulSoup(page, "lxml")

        videos=soup.find_all("div", class_="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix")
        if(len(videos)):
            videoList=[]
            for a in videos: 
                """ print(a.prettify())
                print("\n") """
                listItems=a.ul.find_all("li", recursive=False)
                thumbnail=a.img.get("data-thumb")
                thumbnail=thumbnail if thumbnail else a.img.get("src")
                duration=a.span.text.strip("\n")
                title=a.h3.a.text
                videoList.append({"uploaded": listItems[0].text, "views": listItems[1].text, "thumbnail": thumbnail, "duration": duration, "title": title})

            return videoList
        
        else:
            print("could not find video container on page")
    
    else: 
        print("request failed\n")

#print(searchYoutube("tool", 1))

#print(soup.prettify())

for i in searchYoutube("tool", 1):
    print(i,"\n")