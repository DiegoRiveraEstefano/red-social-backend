from rest_framework import viewsets
from .serializer import PostSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Post
import uuid

# Create your views here.


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

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

    def list(self, request, *args, **kwargs):
        """

        Args:
            request: is the request from the client
            *args:
            **kwargs:

        Returns: this return a list of a posts

        """
        return Response(list(map(lambda post: {
            "uuid": post.uuid,
            "title": post.title,
            "description": post.description,
            "image_url": post.image_url,
            "user": post.user.username
        }, Post.objects.all())))

    def retrieve(self, request, *args, **kwargs):
        """

        Args:
            request: is the request from the client
            *args:
            **kwargs: is the args send by the client, in this case contain de pk of post

        Returns: this return a post by a especific uuid.

        """
        post = Post.objects.filter(uuid=kwargs.get("pk")).values()
        if len(post) == 0:
            return Response(status=404)

        print(post[0])

        return Response(
            post[0]
        )

    def create(self, request, *args):
        """

        Args:
            request: is the request from the client
            *args:

        Returns: this return a response with a status of result of creation the post

        """
        data = request.data
        token = Token.objects.filter(key=request.auth).values()
        if len(token) == 0:
            return Response(status=401)

        user = User.objects.filter(pk=token[0]['user_id']).values()
        if len(user) == 0:
            return Response(status=401)

        new_post = Post.objects.create(
            uuid=uuid.uuid4().__str__(),
            title=data['title'],
            description=data['description'],
            image_url=data['image_url'],
            user=User.objects.get_by_natural_key(user[0]['username'])
        )
        new_post.save()

        return Response(status=201)
