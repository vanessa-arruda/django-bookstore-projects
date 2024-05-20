from django.shortcuts import render
from bookstore import forms, models

# Create your views here.

def index(request):
    books_view = models.Book.objects.all()
    # books_view = models.Book.objects.order_by('title')
    book_dict = {'book_list':books_view}
    return render(request, 'bookstore/index.html', context=book_dict)

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