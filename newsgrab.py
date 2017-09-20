import bs4, requests

def getEETimes():
	newsUrl = ('http://www.eetimes.com/internet-of-things-designline.asp')
	baseUrl = 'www.eetimes.com'
	res = requests.get(newsUrl)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems = soup.select('.biggest')
	link = baseUrl + str(elems[0].a.get('href'))
	title = '#EETimes: ' + str(elems[0].text)
	linklist = [title, link]
	return linklist
	