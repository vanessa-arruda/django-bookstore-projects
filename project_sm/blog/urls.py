from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^reviews/$', views.reviews, name='reviews'),
]