from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonial(models.Model):
    star_count = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    text = models.TextField(max_length=200, default='', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)


 #   def __str__(self):
  #      return self.author




