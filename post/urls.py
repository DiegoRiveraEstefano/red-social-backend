from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import PostView

routers = routers.DefaultRouter()
routers.register(r'post', PostView, 'post')

urlpatterns = [
    path("api/v1/", include(routers.urls)),
    path("docs", include_docs_urls(title="Post Api"))
]
