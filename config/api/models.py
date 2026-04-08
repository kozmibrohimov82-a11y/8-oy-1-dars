from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=4,decimal_places=0)
    color = models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)



