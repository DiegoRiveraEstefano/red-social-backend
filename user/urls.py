from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from .views import UserView

routers = routers.DefaultRouter()
routers.register(r'user', UserView, 'user')

urlpatterns = [
    path("api/v1/", include(routers.urls)),
    path('api/auth/', views.obtain_auth_token),
    path("docs/", include_docs_urls(title="user Api")),
]
