from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Crform, Crmodel, Voteform, Votemodel
from django import forms
# Create your views here.

def hello(r):
    return render(r, 'hello.html')
    

def homeview(r):
    context = {}
    crform = Crform()
    voteform = Voteform()
    votes = Votemodel.objects.all()
    context['crform'] = crform
    context['voteform'] = voteform
    context['votes'] = votes
    return render(r, 'home.html', context)

def submitvote(r):
    if r.method == 'POST':
        form = Voteform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/webapp/home/')
    return HttpResponse('error')

def submitcr(r):
    if r.method == 'POST':
        form = Crform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/webapp/home/')
    return HttpResponse('error')

