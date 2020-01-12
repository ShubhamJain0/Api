from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('home-viewset', views.FirstViewSet, 'home-viewset')


urlpatterns = [
	
	path('home/', views.FirstView.as_view()),
	path('', include(router.urls)),

]