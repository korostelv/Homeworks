from django.urls import reverse

from django.db import models


class Poem(models.Model):
    name = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=False)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.PROTECT)
    theme = models.ForeignKey('Theme', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('text', kwargs={'poem_id': self.pk})


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.surname


class Theme(models.Model):
    theme = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.theme
