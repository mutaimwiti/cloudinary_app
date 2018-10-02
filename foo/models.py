from django.db import models
from cloudinary.models import CloudinaryField


class Foo(models.Model):
    image = CloudinaryField('image')
