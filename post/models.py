from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    uuid = models.CharField(primary_key=True, default=0, max_length=128)
    title = models.CharField(null=False, max_length=128)
    description = models.CharField(null=True, default="", max_length=256)
    image_url = models.URLField(null=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="", null=False)
    """
    :uuid: is the primary key of class, const of a object with 64 of len and is alpha numeric
    :title: title of post
    :description: description of post
    :image_url: is a url of image
    :user: is a foreign key of a user that upload the post
    """

    def __str__(self):
        return f"Post(UUID={self.uuid}, title='{self.title}', description='{self.description}', image_url='{self.image_url}')"
