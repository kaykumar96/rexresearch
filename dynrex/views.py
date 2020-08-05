from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.views import APIView
from dynrex.models import Content, ContentDetails, ContentDetailsImage, ContentDetailsFile,ContentDetailsUrl
from dynrex.contentSerializers import ContentSerializer, ContentDetailsSerializer
from django.db.models import Q
from django.http import JsonResponse
import json
import requests
from bs4 import BeautifulSoup
import json
import datetime
import re
import os
import bs4

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import  TokenAuthentication
# Create your views here.

class contentlist(generics.ListCreateAPIView):
	queryset = Content.objects.all()
	serializer_class = ContentSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]
	def get_queryset(self):
		""" allow rest api to filter by submissions """
		queryset     = Content.objects.all()
		return queryset

class contentshow(generics.RetrieveUpdateDestroyAPIView):
	queryset = Content.objects.all()
	serializer_class = ContentSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]

class contentdetailslist(generics.ListCreateAPIView):
	queryset = ContentDetails.objects.all()
	serializer_class = ContentDetailsSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]
	def get_queryset(self):
		""" allow rest api to filter by submissions """
		queryset     = ContentDetails.objects.select_related('content').all()
		return queryset

class contentdetailsshow(generics.RetrieveUpdateDestroyAPIView):
	queryset = ContentDetails.objects.select_related('content').all()
	serializer_class = ContentDetailsSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]



def tempcontentlist(request):
	content_list = Content.objects.all()
	context = {'content_list':content_list}
	return render(request, 'dynrex/content_list.html', context)	


def tempaddcontentdetails(request, content_id, contentdetails_id=0):
	content_data = Content.objects.get(id=content_id)
	contentdetails_data = []
	if int(contentdetails_id)>0:
		contentdetails_data = ContentDetails.objects.get(id=contentdetails_id)
	context = {'data':content_data, 'contentdetails_data':contentdetails_data}
	print(context)
	return render(request, 'dynrex/add_contentdetails.html', context)	

def tempcontentdetailslist(request, content_id):
	content_data        = Content.objects.get(id=content_id)
	contentdetials_data = ContentDetails.objects.filter(content=content_id).all()
	context = {'content_data': content_data, 'contentdetails_data': contentdetials_data}
	print(context)
	return render(request, 'dynrex/contentdetails_list.html', context)			

def submit_contentdetails(request):
	if request.method == 'POST':
		contentdetails_id = request.POST['hiddenId']
		if contentdetails_id!='':
			contentdetails_data = ContentDetails.objects.get(id = contentdetails_id)
		else:
			contentdetails_data = ContentDetails()
		
		
		contentdetails_data.content_id      = request.POST['content']
		contentdetails_data.heading         = request.POST['heading']
		contentdetails_data.heading_details = request.POST['heading_details']
		# contentdetails_data.file            = request.FILES['file']
		# contentdetails_data.image           = request.FILES['image']
		contentdetails_data.save()
		print(request.FILES.getlist('image'))
		print('~~~~~~~~~~~~~')
		print(request.FILES.getlist('file'))
		for image in request.FILES.getlist('image'):
			contentdetailsimage_data = ContentDetailsImage()
			contentdetailsimage_data.contentdetails = contentdetails_data
			contentdetailsimage_data.upload_image   = image
			contentdetailsimage_data.save()
		for file in request.FILES.getlist('file'):
			contentdetailsfile_data  = ContentDetailsFile()    
			contentdetailsfile_data.contentdetails = contentdetails_data
			contentdetailsfile_data.upload_file    = file
			contentdetailsfile_data.save()	
		return redirect('temp_contentlist')


class JsonLoad(APIView):
	def post(self,request):
		today = datetime.datetime.now()
		url_get= request.GET.get('url', None)
		content_name = url_get.split('/')[3]
		url2 = 'http://rexresearch.com/'
		result = requests.get(url_get).text
		src = result.split('<hr')
		respons = {"urls": [],
						'files':[],
						'images':[],
						'content':[]
						}
		contenr_obj = Content.objects.create(content_name = content_name, added_date = today)
		for content in src:
			soup = BeautifulSoup(content, 'lxml')

			for url_tag in soup.find_all('a', href=True):
				if '.pdf' in url_tag['href']:
					fileurl = url2 +content_name + '/' +url_tag['href']
					respons['files'].append(fileurl)
				else:
					respons['urls'].append(url_tag['href'])
			for img in soup.find_all("img"):
				imgUrls = url2 +content_name+ '/'+img['src']
				respons['images'].append(imgUrls)
			for para in soup.find_all('body'):
				content_para = para.text
				mapping = [ ("\t",""), ("&nbsp;", " "), ("&amp;", "&"), ("<p>", ""), ("</p>", ""), ("<br>", ""), 
					("<ul>",""), ("</ul>",""), ("<ol>",""), ("</ol>",""), ("<li>",", "), ("</li>",""), ("<u>",""), 
					("</u>",""), ("<b>",""), ("</b>",""), ("<i>",""), ("</i>",""), ("\n", " "),("<a>", " "),("</a>", " ")]
				for k, v in mapping:
					content_para = content_para.replace(k, v)
					content_para = content_para.replace("'",'')
			try:
				content_heading = soup.find('div', align='center').text
				#content_heading.extract()
			except:	
			    try:
			        content_heading = soup.find('div', style="text-align: center;").text
			        #content_heading.extract()
			    except:
			        content_heading = None

			content_details = ContentDetails.objects.create(content=contenr_obj,content_heading=content_heading ,content_para = content_para.encode('unicode_escape'),added_date=today)
			for images in respons['images']:
				ContentDetailsImage.objects.create(contentdetails=content_details, upload_image=images)
			for files in respons['files']:
				ContentDetailsFile.objects.create(contentdetails=content_details,upload_file=files)
				
			ContentDetailsUrl.objects.create(contentdetails=content_details,url_name=respons['urls'])
		return JsonResponse(respons,safe=False)

