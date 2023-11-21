from django import forms
from .models import User


class AddUser(forms.ModelForm):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    age = forms.IntegerField(label='Возраст')
    email = forms.EmailField(label='Почта')
    gender = forms.ChoiceField(choices=(('male', 'Мужской'), ('female', 'Женский')),label='Пол')
    address = forms.CharField(widget=forms.Textarea, label='Адрес')
    subscription = forms.BooleanField(label='Хотите ли подписаться на новости?',required=False)

    class Meta:
        model = User
        fields = '__all__'
