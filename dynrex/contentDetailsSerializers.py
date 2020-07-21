from rest_framework import serializers
from dynrex.models import ContentDetails
from django.urls import reverse

	
class ContentDetailsSerializer(serializers.ModelSerializer):
	content_detail_url = serializers.HyperlinkedIdentityField(view_name='content_details_show', read_only=True)
	

	class Meta:		
		fields = '__all__'
		#exclude = ('status', )
		model = ContentDetails
	