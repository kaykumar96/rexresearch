from rest_framework import serializers
from dynrex.models import Content
from django.urls import reverse

	
class ContentSerializer(serializers.ModelSerializer):
	content_url = serializers.HyperlinkedIdentityField(view_name='content_show', read_only=True)
	

	class Meta:		
		fields = '__all__'
		#exclude = ('status', )
		model = Content
	