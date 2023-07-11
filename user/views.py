from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializer import UserSerializer, User

# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        actions = {
            "create": [AllowAny],
            "list": [AllowAny],
            "retrieve": [AllowAny],
            "update": [IsAuthenticated],
            "partial_update": [IsAuthenticated],
            "destroy": [IsAuthenticated],
        }
        permission_classes = actions[self.action] if self.action in actions.keys() else [IsAdminUser]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        """
        Args:
            request: is the request from the client
            *args:
            **kwargs: is the args send by the client, in this case contain de name of user

        Returns: this return a user by name

        """

        user = User.objects.filter(username=kwargs.get("pk")).values()
        if len(user) == 0:
            return Response(status=401)

        return Response(
            user[0]
        )

    def create(self, request, **kwargs):
        """

        Args:
            request: is the request from the client, contains data of form
            **kwargs:

        Returns: this return a response with a status of result.

        """

        user = User.objects.filter(username=request.data['username']).values()
        if len(user) > 0:
            return Response(status=402)

        data = request.data
        new_user = User.objects._create_user(username=data['username'], email=data['email'], password=data['password'])
        new_user.save()
        return Response(status=201)
