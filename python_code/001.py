# Method 1

from selenium import webdriver
driver = webdriver.PhantomJS('phantomjs.exe')
url = 'https://mortuzahossain.github.io/basic-webpage-for-scraping/'
driver.get(url)
html = driver.page_source

print html

# Method 2

import urllib2
url = 'https://mortuzahossain.github.io/basic-webpage-for-scraping/'

openurl = urllib2.urlopen(url)
html = openurl.read()
openurl.close()

print html

