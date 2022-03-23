from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . models import Order, Price, Website,Type
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm

def index(request):
    return render(request, 'pages/index.html')


def categories(request):
    websites = Website.objects.order_by('title')
    types = Type.objects.order_by('title')
    return render(request, 'home/categories.html', {'websites':websites, 'types':types})
    


def zakaz(request, website_id, type_id):
    if Price.objects.filter(website = website_id).filter(type=type_id).exists():
        price = Price.objects.filter(website = website_id).get(type=type_id)
        return render(request, 'home/home.html', {'price':price})



def click(request):
    price_id = request.POST.get('price_id')
    order=Order()
    order.quantity = request.POST.get('quantity')
    order.total = request.POST.get('total')
    order.link = request.POST.get('link')
    order.price = Price.objects.get(id=price_id)
    order.save()
    return redirect(reverse('payment', kwargs={'id':order.id}))



def payment(request,id):

    order = Order.objects.get(id=id)
    return render(request, 'home/click.html', {'order':order})












def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})


def settings(request):
    return render(request, 'pages/settings/index.html')


def user_data(request):
    return render(request, 'pages/settings/data.html')


def workers(request):
    return render(request, 'pages/workers.html')