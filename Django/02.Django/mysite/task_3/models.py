from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, EmailValidator


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)], blank=False)
    surname = models.CharField(max_length=20, validators=[MinLengthValidator(3)], blank=False)
    age = models.IntegerField(validators=[MinValueValidator(18)], blank=False, default=18)
    email = models.EmailField(validators=[EmailValidator], blank=False, default='')
    gender = models.CharField(choices=(('male', 'Мужской'), ('female', 'Женский')), max_length=8, blank=False,
                              default='male')
    address = models.TextField(max_length=200, blank=True)
    subscription = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'