from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegForm
from .forms import SmartphoneEg
from .forms import GeeksForm
from .forms import LoginForm
from .forms import SessLoginForm

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html')


def home_view(request):
    context = {}
    form = RegForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)


def smartphone_view(request):
    context = {}
    form = SmartphoneEg(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)


def geeks_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)

def login_view(request):
    return render(request, 'login.html')


def loggedin_view(request):
    username = "not logged in"
    cn = "not found"
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            cn = MyLoginForm.cleaned_data['contact_num']
    else:
        MyLoginForm = LoginForm()
    context = {'username': username, 'contact_num': cn}
    return render(request, 'loggedin.html', context)


def sessloggedin_view(request):
	username = 'not logged in'
	if request.method == 'POST':
		MyLoginForm = SessLoginForm(request.POST)
		if MyLoginForm.is_valid():
			username = MyLoginForm.cleaned_data['username']
			request.session['username'] = username
	else:
		MyLoginForm = SessLoginForm()
	return render(request, 'sessloggedin.html', {"username" : username})


def sesslogin_view(request):
	if request.session.has_key('username'):
		username = request.session['username']
		return render(request, 'sesslogin.html', {"username" : username})
	else:
		return render(request, 'sesslogin.html', { })
	

def sesslogout_view(request):
	try:
		del request.session['username']
	except:
		pass
	return HttpResponse("<strong>You are logged out.</strong>")