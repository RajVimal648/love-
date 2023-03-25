from django.db import models

# Create your models here.
class Calculate_Love(models.Model):
    fname=models.CharField(max_length=25,primary_key=True)
    sname=models.CharField(max_length=30)
