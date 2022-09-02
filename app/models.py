from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='City', null=True,
                            blank=True)
    members = models.ManyToManyField(User)
    def __str__(self):
        return self.name
