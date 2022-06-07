from django.db import models

# Create your models here.

class foodsList(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'foods'
    
    