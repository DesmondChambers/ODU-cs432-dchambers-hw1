#!/usr/bin/python3
# pdfFinder.py

#                                   References
# King, Code Monkey. “How to Scrape PDF Files Using Python + Requests and BeautifulSoup.” YouTube, 
#       YouTube, 6 June 2020, www.youtube.com/watch?v=VDd6dVrYzao. 
#
#   the above source was used in creating the solution below.
#

# packages
import sys
import requests
from bs4 import BeautifulSoup
import re

# target URL
url = ("{}" . format(sys.argv[1]))

# make HTTP GET request to the target URL
print('\nURI to search: {}\n' .format(url))
response = requests.get(url)

# parse content
content = BeautifulSoup(response.text, 'lxml')

# extract URLs referencing PDF documents
all_urls = content.find_all('a')

# loop over all URLs
for url in all_urls:
    # try URLs containing 'href' attribute
    try:
        # pick up only those URLs containing 'pdf'
        # within 'href' attribute
        if 'pdf' in url['href']:
            # init PDF url
            pdf_url = ''

            pdf_url = url['href']
            pdf_response = requests.get(pdf_url) 

  
            print ("URI: {}".format(pdf_response.request.url))
            print('Final URI: ', pdf_url)   
            print ("Content-Length: {} bytes\n\n".format(pdf_response.headers['Content-Length']))
            
    
    # skip all the other URLs
    except:
        pass