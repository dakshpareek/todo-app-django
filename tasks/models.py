from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(blank=False,max_length=100)
    category_description=models.TextField(blank=False,max_length=500)
