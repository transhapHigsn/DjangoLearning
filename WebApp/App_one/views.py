from django.shortcuts import render
from django.http import HttpResponse
import re
from .models import User

# Create your views here.
User_RE = re.compile(r'^\w{3,15}$')
Nationality_RE = re.compile(r'^\w{5,20}$')


def index(request):
    user = request.session.get('user','new')
    visits = request.session.get('visits',0)
    if visits==0:
        msg = 'Hey newbie, Welcome!'
    else:
        msg = user.capitalize() + ', you\'ve got a liking for this.'

    return render(request,'App_one/index.html',{'message':msg})

def welcome(request):
    username = request.POST['txt']
    request.session['user'] = username
    return render(request, 'App_one/welcome.html',{'username':username})

def next(request, username):
    return render(request, 'App_one/next.html',{'username':username})

def step_one(request):
    username = request.POST['username']
    age = request.POST['age']
    nationality = request.POST['nationality']
    alias = request.POST['alias']

    #validation of input
    if User_RE.match(username):
        if age.isdigit() and int(age)>8:
            if Nationality_RE.match(nationality):
                if User_RE.match(alias):
                    user = User(name = username, age= int(age), nationality=nationality, alias = alias)
                    user.save()

                    return HttpResponse('Information saved successfully.')
                else:
                    error = 'Incorrect alias'
                    return render_form(request,error)
            else:
                error = 'Incorrect nationality input'
                return render_form(request,error)
        else:
            error= 'Either age is not a number or age is less than 8'
            return render_form(request,error)
    else:
        error = 'Incorrect username'
        return render_form(request,error)                

def render_form(request,error=''):
    username = request.POST['username']
    age = request.POST['age']
    nationality = request.POST['nationality']
    alias = request.POST['alias']

    context = {
        'username':username,
        'age':age,
        'nationality':nationality,
        'alias':alias,
        'error':error
    }
    return render(request,'App_one/next.html',context)
