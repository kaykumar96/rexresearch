from bs4 import BeautifulSoup
import requests

# #for html file within directory
# # with open('http://www.rexresearch.com/HDAC1/hdac1.html') as html_file:
# # 	soup = BeautifulSoup(html_file, 'lxml')


# # for global html pages
# source = requests.get('http://www.rexresearch.com/HDAC1/hdac1.html').text

# soup = BeautifulSoup(source, 'html.parser')



# html_body = soup.find('body')
# for content in html_body.find_all('hr'):
# 	print(content.next_siblings)
# 	print(type(content.next_siblings))
# 	print("~~~~~~~~~~~~~~~~~~~~")



############################################################################################################

from urllib.request import urlopen
# import bs4
# import requests
# import json

r = requests.get('http://www.rexresearch.com/HDAC1/hdac1.html')
raw_text=r.text
texts=raw_text.split('<hr width="100%" size="2">')
#print(len(texts))
#print(texts[2])

for content in texts:
    print('~~~~~~~~~~~~~~~~~')
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # print('+++++++++++++++')
    file = None
    try:
    	content_heading = soup.find('div', align='center').text
    except:
    	content_heading = None	
    try:
    	link = soup.find('a', href=True)
    	link = link['href']
    	if '.pdf' in link:
    		file = link
    		link = None
    except:
    	link = None	


    print(content_heading)
    print("+++++++")
    print(link)
    print("++++++++")
    print(file)

    ##collect urls,image,header,content from text variable and replicate the same for all the pages
   

