from bs4 import BeautifulSoup
import requests

with open('http://www.rexresearch.com/HDAC1/hdac1.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

print(soup)	