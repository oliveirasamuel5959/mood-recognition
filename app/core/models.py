from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=255)
    
    class Meta:
        db_table = "users"
    