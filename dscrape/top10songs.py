import requests
from bs4 import BeautifulSoup

billboard_webpage='http://www.billboard.com/charts/hot-100'
request = requests.get(billboard_webpage)
soup = BeautifulSoup(request.text, 'html.parser')
prettyString = soup.prettify().encode('utf-8').strip()
title_instances=soup.find_all('div',attrs={'class':'chart-list-item__title'})
artist_instances=soup.find_all('div',attrs={'class':'chart-list-item__artist'})
titles=[]
artists=[]
for title in title_instances:
    	titles.append(title.text.strip())
for artist in artist_instances:
    	artists.append(artist.text.strip())

top10Titles=titles[:10]
top10Artists=artists[:10]

def getSongAndArtist(song,artist):
    	id=1
    	for i in zip(song,artist):
            	print('#'+str(id),i[0],'by',i[1])
            	id+=1

getSongAndArtist(top10Titles,top10Artists)


