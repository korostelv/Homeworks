from django.db import models


class Login(models.Model):
    name = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    admin_is = models.BooleanField(default=False)

    def __str__(self):
        return self.name
