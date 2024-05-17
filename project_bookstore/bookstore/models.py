from django.db import models

# Create your models here.
#Admin models - Books here

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    publication_date = models.DateField()
    cover_image = models.ImageField()

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {str(self.price)} SEK, Publication Date: {str(self.publication_date)}"
    
#Admin models - Users here
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"Username: {self.name} | Email: {self.email}"

#Admin models - Books here