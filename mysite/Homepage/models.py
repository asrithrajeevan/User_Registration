from django.db import models

# Create your models here.

class Registration(models.Model):
    user_id = models.AutoField(null=False, primary_key=True)
    first_name = models.CharField(max_length=150, null = False)
    last_name = models.CharField(max_length=150, null = True)
    Email = models.EmailField(max_length=150, null = False)
    password = models.CharField(max_length=150, null = False)
    
    