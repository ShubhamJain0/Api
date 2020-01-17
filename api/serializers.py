from rest_framework import serializers
from api import models

class HomeSerializer(serializers.Serializer):
	"""It takes the input, also similar to forms"""
	name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
	"""It takes the input, and saves in the database"""


	class Meta:
		model = models.UserProfile
		fields = ('id','email', 'name', 'password')
		extra_kwargs = {

		'password': {

		'write_only':True,
		'style':{'input_type':'password'}
		}
		}

	def create(self, validated_data):
		"""Creates a new user"""
		user = models.UserProfile.objects.create_user(
			email=validated_data['email'],
			name=validated_data['name'],
			password=validated_data['password']
			)

		return user