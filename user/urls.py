from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import UserView

routers = routers.DefaultRouter()
routers.register(r'user', UserView, 'user')

"""
urls for the user api
"""
urlpatterns = [
    path("api/v1/", include(routers.urls)),
    path('api/auth/', views.obtain_auth_token),
]
