from django.db import models


class Divination(models.Model):
    prediction = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.prediction
