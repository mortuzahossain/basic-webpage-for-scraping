from bs4 import BeautifulSoup
import urllib2
url = 'https://mortuzahossain.github.io/basic-webpage-for-scraping/'

openurl = urllib2.urlopen(url)
html = openurl.read()
openurl.close()

soup = BeautifulSoup(html,'lxml')

print soup.prettify()