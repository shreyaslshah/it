from django.db import models
from django import forms
# Create your models here.


class Crmodel(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Crform(forms.ModelForm):
    class Meta:
        model = Crmodel
        exclude = ()

class Votemodel(models.Model):
    name = models.ForeignKey(Crmodel, on_delete=models.CASCADE)
    vote = models.BooleanField()

class Voteform(forms.ModelForm):
    class Meta:
        model = Votemodel
        exclude = ()