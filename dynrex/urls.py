from django.conf.urls import url,include
# from .views import content, contentdetails
from dynrex.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 

urlpatterns =[
			url(r'^1.0/',
				include([
					url(r'^content/list/$',contentlist.as_view(),name='content_list'),
					url(r'^content/show/(?P<pk>[0-9]+)$',contentshow.as_view(),name='content_show'),

					url(r'^contentdetails/list/$',contentdetailslist.as_view(),name='content_details_list'),
					url(r'^contentdetails/show/(?P<pk>[0-9]+)$',contentdetailsshow.as_view(),name='content_details_show'),

				])),
			url(r'contentlist/', tempcontentlist, name='temp_contentlist'),
			url(r'addcontentdetails/(?P<content_id>\d+)$', tempaddcontentdetails, name='temp_addcontentdetails'),
			url(r'addcontentdetails/submit_contentdetails/$',submit_contentdetails, name='submit_contentdetails'),
			url(r'contentdetailslist/(?P<content_id>\d+)$', tempcontentdetailslist, name='temp_contentdetailslist'),
			
			#url(r'branch/add/(?P<branch_id>\d+)$',views.add_branch, name='edit_branch'),
			]