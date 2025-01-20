from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class book_users(User):
    password_re = models.CharField(max_length=15)
    
