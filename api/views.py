from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HomeSerializer

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