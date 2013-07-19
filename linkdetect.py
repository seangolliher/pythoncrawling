#! /user/bin/python

### Link Finder. Crawls backlinks and looks for registers/logins 
#   Sean Golliher 7/2012
#
#
## Use the urllib2 library for URLs
from BeautifulSoup import BeautifulSoup
import urllib2 
import xlrd 
import sys 
import re #regular expression library with re.search and re.findall etc. 

#open workbook
wb = xlrd.open_workbook('test.xlsx')

#get the sheet names
wb.sheet_names()


#get the name of first sheet 
sh = wb.sheet_by_index(0)

#Iterate throw rows and print
#for rownum in range(sh.nrows):
    #print sh.col_values(rownum)


#Print out only column 2  entries in spreadsheet (python starts at 0 excel at 1 )
for rownum in range(sh.nrows):

 print sh.cell(rownum,1).value
 httpResponse = urllib2.urlopen(sh.cell(rownum,1).value)
 htmlpage = httpResponse.read()
 soup = BeautifulSoup(htmlpage)
for link in soup.find_all('a'):  # find all the links 
       print(link.get('href'))