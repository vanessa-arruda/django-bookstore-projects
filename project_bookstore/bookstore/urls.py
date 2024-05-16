from django.conf.urls import url
from bookstore import views

app_name = 'bookstore'

urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^review/$', views.review, name='review'),
    url(r'^signup/$', views.register, name='register'),
    url(r'login/$', views.login, name='login'),

]
