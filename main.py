import requests
from bs4 import BeautifulSoup
import pafy
import os

search=raw_input('Insert the title and the singer:')

query_string = search.replace(' ','+')
print query_string

response = requests.get('https://www.youtube.com/results?search_query=%s' % query_string)

soup = BeautifulSoup(response.text, 'html.parser')
print soup.prettify()

videos = soup.find_all('a')

links = []
for elem in videos:
	if elem.get('href').startswith('/watch'):
		print 'this is a video'
		links.append(elem.get('href'))


print len(videos)
print links
print len(links)
print links[0]

url = 'https://www.youtube.com'+links[0]
print url
#url = 'https://www.youtube.com/watch?v=CHekNnySAfM'

video = pafy.new(url)

audio = video.audiostreams[2]
audio.download(filepath='./%s'%query_string+'.m4a')

os.system('mplayer ./%s.m4a' % query_string)