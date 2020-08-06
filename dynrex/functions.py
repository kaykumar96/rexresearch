from dynrex.models import Content, ContentDetails, ContentDetailsImage, ContentDetailsFile,ContentDetailsUrl
from django.db.models import Q
from django.http import JsonResponse

import requests
from bs4 import BeautifulSoup
import json
import datetime
import re
import os

def map_unwanted_tags(to_map):
	mapping = [ ('width="100%" size="2">', ""), ("\t",""), ("&nbsp;", " "), ("&amp;", "&"), ("<p>", ""), ("</p>", ""), ("<br>", ""), 
				("<ul>",""), ("</ul>",""), ("<ol>",""), ("</ol>",""), ("<li>",", "), ("</li>",""), ("<u>",""), 
				("</u>",""), ("<b>",""), ("</b>",""), ("<i>",""), ("</i>",""), ("\n", " "),("<a>", " "),("</a>", " ")]
	for k, v in mapping:
		to_map = to_map.replace(k, v)
		to_map = to_map.replace("'",'')
	return to_map

def scrap_rexresearch_url(url_name, content_name, parent_content_id = None):
	today        = datetime.datetime.now()
	result       = requests.get(url_name).text
	result_texts = result.split('<hr')
	content_obj  = Content.objects.create(content_name = content_name, added_date = today)
	if parent_content_id is not None:
		content_obj.parent_content = Content.objects.get(id = parent_content_id)
		content_obj.save()
	page_urls    = []
	for content in result_texts:
		# print('~~~~~~~~~~~~~~~~~')
		soup = BeautifulSoup(content, 'lxml')
		# print(soup)
		# print('+++++++++++++++')
		file      = None
		img_list  = []
		file_list = []
		url_list  = []
		try:
			content_heading = soup.find('div', align='center').text
			#content_heading.extract()
		except:	
		    try:
		        content_heading = soup.find('div', style="text-align: center;").text
		        #content_heading.extract()
		    except:
		        content_heading = None
		try:
		    for url in soup.find_all('a', href=True):
		        if '.pdf' in url['href'] and 'https://' not in url['href']:
		            file_list.append(url['href'])
		        else:
		            url_dict = {url.text : url['href']}
		            url_list.append(url_dict)
		            url_comp_list = url['href'].split('/')
		            if (len(url_comp_list)==1 and '#' not in url_comp_list[0]):
		                page_urls.append(url_dict)
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

		# print(content_heading)
		# print("+++++++")
		# print(url_list)
		# print("++++++++")
		# print(file_list)
		# print("+++++++++")
		# print(img_list)	
		response = {
					'content_heading' : content_heading,
					'url_list'        : url_list,
					'file_list'       : file_list,
					'img_list'        : img_list 
					}
		if content_heading is not None:
			content_heading = map_unwanted_tags(content_heading)
			content_para    = content_para.replace(content_heading, '')
			# mapping = [ ("\t",""), ("&nbsp;", " "), ("&amp;", "&"), ("<p>", ""), ("</p>", ""), ("<br>", ""), 
			# 	("<ul>",""), ("</ul>",""), ("<ol>",""), ("</ol>",""), ("<li>",", "), ("</li>",""), ("<u>",""), 
			# 	("</u>",""), ("<b>",""), ("</b>",""), ("<i>",""), ("</i>",""), ("\n", " "),("<a>", " "),("</a>", " ")]
			# for k, v in mapping:
			# 	content_heading = content_heading.replace(k, v)
			# 	content_heading = content_heading.replace("'",'')
			content_details = ContentDetails.objects.create(content=content_obj, content_heading=content_heading.encode('unicode_escape') ,content_para = content_para.encode('unicode_escape'),added_date=today)
			if len(img_list)>0:
				for img in img_list:
					ContentDetailsImage.objects.create(contentdetails=content_details, upload_image=img)
			if len(file_list)>0:
				for file in file_list:
					ContentDetailsFile.objects.create(contentdetails=content_details,upload_file=file)
			if len(url_list)>0:
				for url in url_list:
					[(k,v)] = url.items()
					ContentDetailsUrl.objects.create(contentdetails=content_details,url_name=v)	
	scrapped_response = {"page_url_list" : page_urls, 'content_obj_id': content_obj.id}	
	print(page_urls)
	if (len(page_urls)>0):	
		print("GG")
		url_get_list  = url_name.split('/')
		base_url_list = url_get_list[0:-1]
		base_url      = '/'.join(base_url_list)
		for each_url_dict in page_urls:
			[(sub_content_name, sub_url_get)] = each_url_dict.items()
			sub_url_get  = base_url+'/'+sub_url_get
			sub_responce = scrap_rexresearch_url(sub_url_get, sub_content_name, content_obj.id)
	return scrapped_response				