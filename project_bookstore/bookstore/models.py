from django.db import models
import datetime

# Create your models here.
#Admin models - Books here

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_cover')

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {str(self.price)} SEK, Publication Date: {str(self.publication_date)}"
    
#Admin models - Users here
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"Username: {self.name} | Email: {self.email}"

#Admin models - Orders here

class Order(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    address = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.today)
    order_status = models.BooleanField(default=False)

    def place_order(self):
        self.save()
    
    def __str__(self):
        return f"The order of {self.quantity} - {self.product} is {self.order_status}"