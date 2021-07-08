from django.db import models

class Image(models.Model):
    img = models.ImageField(upload_to="myimg")
    date = models.DateTimeField(auto_now_add=True)
