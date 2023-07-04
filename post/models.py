from django.db import models

class Post(models.Model):
    uuid = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(null=False, max_length=128)
    description = models.CharField(null=True, default="", max_length=256)
    image_url = models.URLField(null=True, default="")

    def __str__(self):
        return f"Post(UUID={self.uuid}, title='{self.title}', description='{self.description}', image_url='{self.image_url}')"
    
    
