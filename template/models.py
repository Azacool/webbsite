from django.db import models

class Customer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name= models.CharField(max_length=30,default=False,blank=False)
    last_name= models.CharField(max_length=30,default=False,blank=True)
    image= models.ImageField(upload_to='template/static/images/')
    
    
