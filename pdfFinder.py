# packages
import requests
from bs4 import BeautifulSoup
import re

# target URL
url = 'https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html'

# make HTTP GET request to the target URL
print('URI to search: ', url)
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