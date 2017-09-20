from bs4 import BeautifulSoup
from urllib2 import urlopen
import os, imgwrite, requests, textwrap, random

def getData(count):
	BASE_URL = "https://interfacelift.com"
	url = 'https://interfacelift.com/wallpaper/downloads/date/wide_16:9/1920x1080/'
	html = urlopen(url).read()
	
	soup = BeautifulSoup(html, 'html.parser')
	elems = soup.select('.item')
	
	picdata = []
	for elem in elems:
		title = str(elem.h1.text)
		dl = elem.select('.download')[0]
		link = BASE_URL + dl.a.get('href')
		by = unicode('by ') + elem.select('.details')[0].find_all('a')[1].text
		text = elem.find('p').text
		lines = textwrap.wrap(text, width = 128, break_long_words = False)
		text = '\n'.join(lines)
		text = '\n'.join([by, text])
		picinfo = [title, text, link]
		picdata.append(picinfo)
	return picdata[:min(len(elems), count)]
	
		
def saveLinks(picData, writeOn=True):
	try:
		os.chdir(os.getcwd() + "\wallpapers")
	
	except OSError as e:
		os.makedirs(os.getcwd() + "\wallpapers")
		os.chdir(os.getcwd() + "\wallpapers")
	
	dataOut = []
	for set in picData:
		title = set[0]
		text = set[1]
		link = set[2]
		filename = str(link[link.rfind('/') + 1:])
		if os.path.isfile(filename):
			print "Already Saved"
		else:
			f = open(filename, 'wb')
			f.write(urlopen(link).read())
			f.close()
	
			if writeOn:
				imgwrite.wallpaper(filename, set[0], set[1])
		filepath = str(os.getcwd() + '\\'+ filename)
		dataOut.append([title, text, filepath])	
	return dataOut	

def grabOne():
	data = saveLinks(getData(1))[0]
	filename = data[2]
	title = data[0]
	
	return (title, filename)
	
def grabRandom():
	index = random.randint(0,9)
	data = saveLinks(getData(10))[index]
	filename = data[2]
	title = data[0]
	
	return (title, filename)
