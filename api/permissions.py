from rest_framework import permissions




class UserProfilePermission(permissions.BasePermission):
	"""allows user to edit their own profile"""

	def has_object_permission(self, request, view, obj):
		"""checks whether the user is editing their own profile"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.id == request.user.id



class ProfileFeedPermission(permissions.BasePermission):
	"""allows user to edit their feed"""


	def has_object_permission(self, request, view, obj):
		"""checks whether the user is editing their own feed"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user_profile.id == request.user.id