from rest_framework import generics
from dynrex.models import Content
from dynrex.contentSerializers import ContentSerializer
from django.db.models import Q
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import  TokenAuthentication


class list(generics.ListCreateAPIView):
	queryset = Content.objects.filter(status=0).all()
	serializer_class = ContentSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]


	def get_queryset(self):
		""" allow rest api to filter by submissions """
		queryset     = Content.objects.all()
		return queryset

class show(generics.RetrieveUpdateDestroyAPIView):
	queryset = Content.objects.all()
	serializer_class = ContentSerializer
	# permission_classes = [IsAuthenticated,]
	# authentication_classes = [TokenAuthentication]

