from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarModelForm, FirstPageForm, Q3Form, Q4Form

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html')


def q1_1_view(request):
    context = {}
    form = CarModelForm()
    context['form'] = form
    return render(request, "q1_1.html", context)


def q1_2_view(request):
    manafacturer = "not logged in"
    model_name = "not found"
    if request.method == "POST":
        # Get the posted form
        Form = CarModelForm(request.POST)
        if Form.is_valid():
            manafacturer = Form.cleaned_data['manufacturer']
            model_name = Form.cleaned_data['model_name']
            print(manafacturer, model_name)
    else:
        Form = CarModelForm()
    context = {'manafacturer': manafacturer, 'model_name': model_name}
    return render(request, 'q1_2.html', context)


def q2_1_view(request):
    if request.session.has_key('name'):
        del request.session['name']

    context = {}
    form = FirstPageForm(request.POST or None)
    context['form'] = form
    return render(request, 'q2_1.html', context)


def q2_2_view(request):
    name = 'not logged in'
    roll = 'not logged in'
    subjects = 'not logged in'
    if request.method == 'POST':
        Form = FirstPageForm(request.POST)
        if Form.is_valid():
            name = Form.cleaned_data['name']
            roll = Form.cleaned_data['roll']
            subjects = Form.cleaned_data['subjects']
            request.session['name'] = name
            request.session['roll'] = roll
            request.session['subjects'] = subjects
    else:
        Form = FirstPageForm()
    context = {'name': name, 'roll': roll, 'subjects': subjects}
    return render(request, 'q2_2.html', context)


def q3_1_view(request):
    context = {}
    form = Q3Form(request.POST or None)
    context['form'] = form
    return render(request, "q3_1.html", context)


def q3_2_view(request):
    username = "not logged in"
    email = "not found"
    contact = "not found"
    if request.method == "POST":
        # Get the posted form
        Form = Q3Form(request.POST)
        if Form.is_valid():
            username = Form.cleaned_data['username']
            email = Form.cleaned_data['email']
            contact = Form.cleaned_data['contact']
    else:
        Form = Q3Form()
    context = {'username': username, 'email': email, 'contact': contact}
    return render(request, 'q3_2.html', context)


def q4_1_view(request):
    context = {}
    form = Q4Form(request.POST or None)
    context['form'] = form
    return render(request, "q4_1.html", context)


def q4_2_view(request):
    bill = 'null'
    if request.method == "POST":
        # Get the posted form
        Form = Q4Form(request.POST)
        if Form.is_valid():
            brand = Form.cleaned_data['brand']
            items = Form.cleaned_data['items']
            quantity = Form.cleaned_data['quantity']
            PRICES = {
                'HP': {'mobile': 10000, 'laptop': 50000},
                'Nokia': {'mobile': 8000, 'laptop': 0},
                'Samsung': {'mobile': 15000, 'laptop': 70000},
                'Motorola': {'mobile': 12000, 'laptop': 0},
                'Apple': {'mobile': 50000, 'laptop': 100000},
            }
            bill = 0
            for item in items:
                bill += PRICES[brand][item] * quantity

    else:
        Form = Q3Form()
    context = {'bill': bill}
    return render(request, 'q4_2.html', context)
