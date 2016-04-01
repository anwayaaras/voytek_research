import lxml
from lxml import html
import requests
from selenium import webdriver




def scrape_website_xpathquery(website,xpath_query):
	#page = requests.get(website)				#requests.get('http://econpy.pythonanywhere.com/ex/001.html')
	#tree = html.fromstring(page.content)
	#data = tree.xpath(xpath_query)

	path_to_chromedriver = "/Users/anwaya/Downloads/chromedriver"
	browser = webdriver.Chrome(executable_path = path_to_chromedriver)
	browser.get(website)
	browser.find_element_by_xpath(xpath_query)

	  
	browser.quit()
	return results


def try2():
	import lxml
	from lxml import html

	from lxml.cssselect import CSSSelector
	import requests
	page = requests.get('http://www.genecards.org/cgi-bin/carddisp.pl?gene=DRD2&keywords=D2')
	tree = html.fromstring(page.content)
	data=tree.xpath('//*[@id="_summaries"]/div[2]/p')
	
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
	print data


try2()


if __name__ == "__main__":
	
	website = "http://www.genecards.org/cgi-bin/carddisp.pl?gene=DRD2&keywords=D2"
	query = '//*[@id="_summaries"]/div[1]/ul/li/p'
	entrez = scrape_website_xpathquery(website,query)
	print entrez

"""
//*[@id="_summaries"]/div[1]/ul/li/p

/html/body/div[5]
/html/body/div[5]/div
website = "http://econpy.pythonanywhere.com/ex/001.html"
	query = '//div[@title="buyer-name"]/text()'
	buyers = scrape_website_xpathquery(website,query)
	print buyers

"""