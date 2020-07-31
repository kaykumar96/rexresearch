import requests
from bs4 import BeautifulSoup
import json
from os.path  import basename
import re
import os

url = 'http://rexresearch.com/invnindx.htm'
url2 = 'http://rexresearch.com/'
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'lxml')
respons = {"urls": [],
			'files':[],
			'images':[],
			'content':[]
			}

for url_tag in soup.find_all('a', href=True):
	if '.pdf' in url_tag['href']:
		fileurl = url + '/' +url_tag['href']
		respons['files'].append(fileurl)
	else:
		respons['urls'].append(url_tag['href'])
for header in soup.find_all('div'):
	respons['content'].append(header.text)
for img in soup.find_all("img"):
	imgUrls = url + '/' +img['src']
	respons['images'].append(imgUrls)

# respons2 = {"urls": [],
# 					'files':[],
# 					'images':[],
# 					'content':[]}

for urls_in in respons['urls']:
	if urls_in != 'index.htm' and urls_in !='#inventor' and urls_in != '#subject':
		print(url2+urls_in)
		name = urls_in.split('.')[0]
		result2 = requests.get(url2+urls_in)
		src2 = result2.content
		soup2 = BeautifulSoup(src2, 'lxml')
		respons2 = {"urls": [],
					'files':[],
					'images':[],
					'content':[],
					'p_tag_content':[]
					}
		for url_tag1 in soup2.find_all('a', href=True):
			respons2['urls'].append(url_tag1['href'])
			if '.pdf' in url_tag1['href']:
				fileurl = url + '/' +url_tag1['href']
				respons2['files'].append(fileurl)
			
		for header in soup2.find_all('div'):
			respons2['content'].append(header.text)

		for img in soup2.find_all("img"):
			imgUrls = url2 + urls_in.split('.')[0].split('/')[0]+ '/' +img['src']
			respons2['images'].append(imgUrls)

		for i in soup2.findAll('p'):
			respons2['p_tag_content'].append(i.text)

		# print(respons2['p_tag_content'])
		#creating folder & file based on url name and data dump into the file
		dirname = os.path.dirname(name)
		if not os.path.exists(dirname):
			os.makedirs(dirname)
			file = open("{}.txt".format(name), "w+")
			file.write(json.dumps(respons2))
			file.close()


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



# download images code

# if not imgUrls.endswith('.gif'):
	#     print(imgUrls)
	#     # urls = 'http://rexresearch.com/bang.png'
	#     local_image_filename = wget.download(imgUrls)
# r = requests.get(urls, allow_redirects=True)
# open('bernays.jpg', 'wb').write(r.content)