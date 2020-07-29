import requests
from bs4 import BeautifulSoup
import json
from os.path  import basename
import re
import wget
url = 'http://rexresearch.com/stuff/72020stuff/72020stuff.html'
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'lxml')
respons = {"urls": [],
                    'files':[],
                    'images':[],
                    'content':[]}
bTags =[]
for url_tag in soup.find_all('a', href=True):
    respons['urls'].append(url_tag['href'])
    if '.pdf' in url_tag['href']:
        fileurl = url + '/' +url_tag['href']
        respons['files'].append(fileurl)
        # link = None
for header in soup.find_all('div'):
    respons['content'].append(header.text)

# for i in soup.findAll('b'):
#     bTags.append(i.text)
# print(bTags)
for img in soup.find_all("img"):
    imgUrls = url + '/' +img['src']
    # if not imgUrls.endswith('.gif'):
    #     print(imgUrls)
    #     # urls = 'http://rexresearch.com/bang.png'
    #     local_image_filename = wget.download(imgUrls)
# r = requests.get(urls, allow_redirects=True)
# open('bernays.jpg', 'wb').write(r.content)
       
respons['images'].append(imgUrls)
   
file = open("Inventor & Subject Index .txt", "w")
file.write(json.dumps(respons))
file.close()
# print(respons['urls'])


# pages = []
# if respons['urls']:
#     for i in respons['urls']:
#         links = i.startswith('/')
#         if links == True:
#             pages.append(url + str(i))
# print(pages)
# for page in pages:
    
# result2 = requests.get('')
# src2 = result2.content
# soup2 = BeautifulSoup(src2, 'lxml')
# respons2 = {"urls": [],
#             'files':[],
#             'images':[],
#             'content':[]}
# for url_tag2 in soup2.find_all('a', href=True):
#     print(url_tag2['href'])
            
                        
#                 respons2['urls'].append(url_tag2['href'])
# print(respons2['urls'])

