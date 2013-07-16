#! /user/bin/python

### Basic Web Crawler in Python to Grab a URL from command line
#   Sean Golliher 1/2012
#
## Use the urllib2 library for URLs

from BeautifulSoup import BeautifulSoup
import sys   #allow users to input string
import urllib2

####change user-agent name
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
   version = 'gollibot/1.0'
print MyOpener.version  # print the user agent name 
######
httpResponse = urllib2.urlopen(sys.argv[0])

#store html page in an object called htmlPage

htmlPage = httpResponse.read()

print htmlPage

from BeautifulSoup import BeautifulSoup

htmlDom = BeautifulSoup(htmlPage)

# dump page title 

print htmlDom.title.string

# dump all links in page 

allLinks = htmlDom.findAll('a', {'href': True})
for link in allLinks:
	print link['href']

MyOpener.version	
