from django.shortcuts import reverse
from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand/%y/%m/%d/')
    slug = models.SlugField(unique=True)
    # unique = yangi element slugi eski elementlar ichida bolmasa kegin saqledi

    def __str__(self):
        return f"{self.title}"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/%y/%m/%d/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:car_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"


