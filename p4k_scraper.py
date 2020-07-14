import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://pitchfork.com/features/lists-and-guides/best-albums-2019/'

#opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")
containers = page_soup.body.div

filename = "p4k_top_50_albums.csv"
f = open(filename, "w")

headers = "Rank, Artist, Album\n"
f.write(headers)

i = 0
while i < 50:
    
    container = containers.findAll("h2")
    container_rank = containers.findAll("div", {"class":"heading-h3"})
    rank = container_rank[i].text.replace(".","")
    artist_album = container[i].text
    split_string = artist_album.split(":")
    artist = split_string[0]
    album = split_string[1]
    i = i+1

    f.write(rank + "," + artist + "," + album + "\n")

f.close()
