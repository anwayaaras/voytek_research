def cssselector():
	pass
	import lxml.html
	from lxml.cssselect import CSSSelector

	# get some html
	import requests

	r = requests.get('http://www.genecards.org/cgi-bin/carddisp.pl?gene=DRD2&keywords=D2')

	# build the DOM Tree
	tree = lxml.html.fromstring(r.text)

	# print the parsed DOM Tree
	print lxml.html.tostring(tree)

	# construct a CSS Selector
	sel = CSSSelector('#_summaries > div:nth-child(2) > ul > li > p')

	# Apply the selector to the DOM tree.
	results = sel(tree)
	print results

	# print the HTML for the first result.
	match = results[0]
	print lxml.html.tostring(match)

	# get the href attribute of the first result
	print match.get('href')

	# print the text of the first result.
	print match.text

	# get the text out of all the results
	data = [result.text for result in results]


def bs(website):
	from bs4 import BeautifulSoup
	import urllib
	r = urllib.urlopen(website).read()
	soup = BeautifulSoup(r)
	# summary=soup.find_all("div", class_="gc-subsection")
	import pdb;pdb.set_trace()
	# p_nodes = soup.find_all('//*[@id="_summaries"]/div/ul/li/p')
	p_nodes = soup.find_all("section", id="_summaries")
	print p_nodes


bs('http://www.ncbi.nlm.nih.gov/gene/?term=D2')
