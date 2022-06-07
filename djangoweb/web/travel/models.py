from django.db import models

# Create your models here.

class travelList(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    price = models.IntegerField()
    link = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    infotxt = models.TextField()
    
    class Meta:
        db_table = "travel"
    