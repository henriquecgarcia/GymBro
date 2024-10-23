from . import views
from django.urls import path

urlpatterns = [
	path('test/', views.test, name='test'),
	path('register/', views.register, name='register'),
]