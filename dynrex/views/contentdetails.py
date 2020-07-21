from rest_framework import generics
from dynrex.models import ContentDetails
from dynrex.contentDetailsSerializers import ContentDetailsSerializer
from django.db.models import Q
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import  TokenAuthentication


class list(generics.ListCreateAPIView):
	queryset = ContentDetails.objects.all()
	serializer_class = ContentDetailsSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]


	def get_queryset(self):
		""" allow rest api to filter by submissions """
		queryset     = ContentDetails.objects.select_related('content').all()
		return queryset

class show(generics.RetrieveUpdateDestroyAPIView):
	queryset = ContentDetails.objects.select_related('content').all()
	serializer_class = ContentDetailsSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]

