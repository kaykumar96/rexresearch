from django.conf.urls import url,include
# from .views import content, contentdetails
from dynrex.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
			url(r'^1.0/',
				include([
					url(r'^content/list/$',contentlist.as_view(),name='content_list'),
					url(r'^content/show/(?P<pk>[0-9]+)$',contentshow.as_view(),name='content_show'),

					url(r'^contentdetails/list/$',contentdetailslist.as_view(),name='content_details_list'),
					url(r'^contentdetails/show/(?P<pk>[0-9]+)$',contentdetailsshow.as_view(),name='content_details_show'),

				])),
			]