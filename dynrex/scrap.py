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

r         = requests.get('http://www.rexresearch.com/saphonian/aouini.htm')
raw_text  = r.text
# page_soup = BeautifulSoup(raw_text, 'lxml')
# hr_tag    = page_soup.find('hr')
# print(str(hr_tag))
texts     = raw_text.split('<hr')
#print(len(texts))
# print(raw_text)
#print(texts[2])

def map_unwanted_tags(to_map):
    mapping = [ ("\t",""), ("&nbsp;", " "), ("&amp;", "&"), ("<p>", ""), ("</p>", ""), ("<br>", ""), 
                ("<ul>",""), ("</ul>",""), ("<ol>",""), ("</ol>",""), ("<li>",", "), ("</li>",""), ("<u>",""), 
                ("</u>",""), ("<b>",""), ("</b>",""), ("<i>",""), ("</i>",""), ("\n", " "),("<a>", " "),("</a>", " ")]
    for k, v in mapping:
        to_map = to_map.replace(k, v)
        to_map = to_map.replace("'",'')
    return to_map   

for content in texts:
    print('~~~~~~~~~~~~~~~~~')
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # print('+++++++++++++++')
    
    img_list        = []
    file_list       = []
    url_list        = []
    try:
        content_heading = soup.find('div', align='center').text
        #content_head.extract()
    except:	
        try:
            content_heading = soup.find('div', style="text-align: center;").text 
            #content_head.extract()
        except:
            content_heading = None
           
    try:
        for url in soup.find_all('a', href=True):
            if '.pdf' in url:
                file_list.append(url['href'])
            else:
                url_list.append(url['href'])
            url.extract()    
    except:
        pass                

    try:
        for img in soup.find_all("img"):
            img_list.append(img['src'])
            img.extract()
    except:
        pass        
    
    content_para = soup.text
    content_para = map_unwanted_tags(content_para)

    if content_heading is not None:
        content_heading = map_unwanted_tags(content_heading)
        content_para    = content_para.replace(content_heading,'')

    print("content_heading :")
    print(content_heading)
    print("")
    print("url list :")
    print(url_list)
    print("")
    print("file list :")
    print(file_list)
    print("")
    print("image list :")
    print(img_list)
    print("")
    print("content paragraph :")
    print(content_para)

    ##collect urls,image,header,content from text variable and replicate the same for all the pages
   

