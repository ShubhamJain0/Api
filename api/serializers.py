from rest_framework import serializers


class HomeSerializer(serializers.Serializer):
	"""It takes the input, also similar to forms"""
	name = serializers.CharField(max_length=10)