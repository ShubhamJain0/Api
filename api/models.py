from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
	"""manages the below model"""

	def create_user(self, email, name, password=None):

		if not email:
			raise ValidationError('Please enter a valid email address!')

		email = self.normalize_email(email)
		user = self.model(email=email,name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""creates superuser"""

		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""user model"""
	email = models.EmailField(max_length=200,unique=True)
	name = models.CharField(max_length=180)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)


	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']


	def get_fullname(self):
		"""returns full name"""
		return self.name

	def get_shortname(self):
		"""returns short name"""
		return self.name

	def __str__(self):
		"""returns str of email"""
		return self.email
