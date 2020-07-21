from django.conf.urls import url,include
from .views import content, contentdetails

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
			url(r'^1.0/',
				include([
					url(r'^content/list/$',content.list.as_view(),name='content_list'),
					url(r'^content/show/(?P<pk>[0-9]+)$',content.show.as_view(),name='content_show'),

					url(r'^contentdetails/list/$',content.list.as_view(),name='content_details_list'),
					url(r'^contentdetails/show/(?P<pk>[0-9]+)$',content.show.as_view(),name='content_details_show'),

				])),
			]