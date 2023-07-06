from django.db import models

class food(models.Model):
    name = models.CharField(max_length=50,default='')
    description = models.TextField(default='')  # Add a default value
    price = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='food_images/')

