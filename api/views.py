from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import (HomeSerializer, UserProfileSerializer)
from api import models
from api import permissions


# Create your views here.

class FirstView(APIView):
	"""An Apiview class"""
	serializer_class = HomeSerializer

	def get(self, request, format=None):
		"""Takes a get request and returns a response!"""

		return Response({'message':'Hello!'})

	def post(self, request, format=None):
		"""Requests the input which can be used in our logic"""
		serializer = self.serializer_class(data=request.data)  

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			return Response({'message':f'Hello {name}'})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""It replaces the entire object"""
		return Response({'message':'done!'})

	def patch(self, request, pk=None):
		"""It is used the update the specified object"""
		return Response({'message':'done!'})

	def delete(self, request, pk=None):
		"""It deletes the specified object"""
		return Response({'message':'done!'})





class FirstViewSet(viewsets.ViewSet):
	"""An ViewSet class"""
	serializer_class = HomeSerializer


	def list(self, request):
		"""It returns a response"""
		return Response({'message':'Hello'})

	def create(self, request):
		"""It is similar to post method in APIView"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			return Response({'message':f'Hello {name}'})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
				)

	def retreive(self, request, pk=None):
		"""It is similar to get method in APIView, but it retrieves based on primary key"""
		return Response({'method':'GET'})

	def update(self, request, pk=None):
		"""It is similar to put method in APIView, it updates the entire object"""
		return Response({'method':'PUT'})

	def partial_update(self, request, pk=None):
		"""It is similar to patch method in APIView, it updates part of the object"""
		return Response({'method':'PATCH'})

	def destroy(self, request, pk=None):
		"""It is similar to delete method in APIView"""
		return Response({'method':'delete'})




class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handles the serializer and queryset"""
	serializer_class = UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UserProfilePermission,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email')


class UserProfileAuthentication(ObtainAuthToken):
	"""Handles the authentication of the users"""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
