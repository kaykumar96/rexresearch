from rest_framework import serializers
from dynrex.models import Content, ContentDetails
from django.urls import reverse

	
class ContentSerializer(serializers.ModelSerializer):
	content_url = serializers.HyperlinkedIdentityField(view_name='content_show', read_only=True)
	

	class Meta:		
		fields = '__all__'
		#exclude = ('status', )
		model = Content
	
class ContentDetailsSerializer(serializers.ModelSerializer):
	content_detail_url = serializers.HyperlinkedIdentityField(view_name='content_details_show', read_only=True)
	

	class Meta:		
		fields = '__all__'
		#exclude = ('status', )
		model = ContentDetails
	