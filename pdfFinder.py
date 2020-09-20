#!/usr/bin/python3
# pdfFinder.py

import sys
from bs4 import BeautifulSoup
import requests
import re

address = sys.argv[1]

response = requests.get(address, params={'q': 'LSU'})

pattern = re.compile('\/url\?q=([^&]+)')

soup = BeautifulSoup(response.text)
for links in soup.find_all('a'):
  href = links.get('href')
  m = pattern.match(href)
  if (m != None):
    print (m.groups()[0])