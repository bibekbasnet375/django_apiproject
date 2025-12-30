from django.db import models

class Myproduct(models.Model):
    name= models.TextField()
    sector= models.CharField(max_length=100)
    price= models.IntegerField()
    description= models.TextField()


