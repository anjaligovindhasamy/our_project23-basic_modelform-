from django.db import models

# Create your models here.

class Country(models.Model):
    c_name=models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        return self.c_name
    
class Capital(models.Model):
    c_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    dist_name=models.CharField(max_length=100)

    def __str__(self):
        return self.dist_name