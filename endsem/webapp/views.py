from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import dbmodel, dbform

# Create your views here.


def hello(r):
    return render(r, "hello.html")


class Form(forms.Form):
    boolean = forms.BooleanField(label="boolean field", required=False)
    char = forms.CharField(label="char field")
    choice = forms.ChoiceField(label="choice field", choices=[("c1", "1"), ("c2", "2")])
    integer = forms.IntegerField(label="integer field")


def formview(r):
    context = {}
    form = Form()
    context["form"] = form
    return render(r, "hello.html", context)


def formsubmit(r):
    if r.method == "POST":
        f = Form(r.POST)
        if f.is_valid():
            return render(
                r,
                "formsubmit.html",
                {
                    "boolean": f.cleaned_data["boolean"],
                    "char": f.cleaned_data["char"],
                    "choice": f.cleaned_data["choice"],
                    "integer": f.cleaned_data["integer"],
                },
            )
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


def db1(r):
    context = {}
    objs = dbmodel.objects.all()
    form = dbform()
    context["form"] = form
    context["objs"] = objs
    context["formget"] = Formget()
    context["formfilter"] = Formfilter()
    context["formupdate"] = Formupdate()
    context["formdelete"] = Formdelete()
    return render(r, "db1.html", context)


def db2(r):
    if r.method == "POST":
        form = dbform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/webapp/db1/")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


class Formget(forms.Form):
    name = forms.CharField()
    
class Formfilter(forms.Form):
    name = forms.CharField()
    
class Formupdate(forms.Form):
    name = forms.CharField()
    newname = forms.CharField()

class Formdelete(forms.Form):
    name = forms.CharField()


def dbget(r):
    name = ""
    context = {}
    if r.method == "POST":
        form = Formget(r.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            obj = dbmodel.objects.get(name=name)
            context["obj"] = obj
            return render(r, "dbget.html", context)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


def dbfilter(r):
    name = ""
    context = {}
    if r.method == "POST":
        form = Formget(r.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            objs = dbmodel.objects.filter(name=name)
            context["objs"] = objs
            return render(r, "dbfilter.html", context)
        else:
            print('e1')
            return HttpResponse("error")
    else:
        print('e2')
        return HttpResponse("error")

def dbupdate(r):
    if r.method == "POST":
        form = Formupdate(r.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            newname = form.cleaned_data['newname']
            obj = dbmodel.objects.get(name = name)
            obj.name = newname
            obj.save()
            return HttpResponseRedirect("/webapp/db1/")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")
    
def dbdelete(r):
    if r.method == "POST":
        form = Formdelete(r.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dbmodel.objects.get(name = name).delete()
            return HttpResponseRedirect("/webapp/db1/")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")