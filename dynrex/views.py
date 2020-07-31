from django.shortcuts import render,redirect
from rest_framework import generics
from dynrex.models import Content, ContentDetails, ContentDetailsImage, ContentDetailsFile
from dynrex.contentSerializers import ContentSerializer, ContentDetailsSerializer
from django.db.models import Q
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