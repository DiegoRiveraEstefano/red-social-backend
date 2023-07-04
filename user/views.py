from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer, User

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):

        user = User.objects.filter(username=kwargs.get("pk")).values()
        if len(user) == 0:
            return 404

        return Response(
            user[0]
        )      


        