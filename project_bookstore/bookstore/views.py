from django.shortcuts import render
from bookstore import forms

# Create your views here.

def index(request):
    return render(request, 'bookstore/index.html')

def register(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error - form invalid!')
    return render(request,'bookstore/registration.html', {'form':form})

def login(request):
    return render(request, 'bookstore/login.html')

def cart(request):
    return render(request, 'bookstore/cart.html')

def review(request):
    return render(request, 'bookstore/review.html')

def base(request):
    return render(request, 'bookstore/base.html')