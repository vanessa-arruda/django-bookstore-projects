from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def reviews(request):
    return render(request, 'blog/reviews.html')

def contact(request):
    return render(request, 'blog/contact.html')

def base(request):
    return render(request, 'blog/base.html')
