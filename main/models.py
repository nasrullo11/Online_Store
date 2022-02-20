from django.db import models

class Shoes_collection(models.Model):
    img = models.ImageField(upload_to='images')
    image_title = models.CharField(max_length=255)
    price = models.CharField(max_length=255) 

    def __str__(self):
        return self.image_title

class Racing_boot(models.Model):
    img = models.ImageField(upload_to='images')
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.price

class Product(models.Model):
    img = models.ImageField(upload_to='images')
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.price
