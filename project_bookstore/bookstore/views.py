from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bookstore/index.html')

def register(request):
    return render(request, 'bookstore/registration.html')

def login(request):
    return render(request, 'bookstore/login.html')

def cart(request):
    return render(request, 'bookstore/cart.html')

def review(request):
    return render(request, 'bookstore/review.html')

def base(request):
    return render(request, 'bookstore/base.html')