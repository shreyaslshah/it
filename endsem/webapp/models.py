from django.db import models
from django import forms


# Create your models here.
class dbmodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)


class dbform(forms.ModelForm):
    class Meta:
        model = dbmodel
        exclude = ()
