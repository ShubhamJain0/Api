from django.contrib import admin
from .models import (UserProfile, ProfileStatusFeed)

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ProfileStatusFeed)
