from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('home-viewset', views.FirstViewSet, 'home-viewset')
router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
	
	path('home/', views.FirstView.as_view()),
	path('login/', views.UserProfileAuthentication.as_view()),
	path('', include(router.urls)),

]