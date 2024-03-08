from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    
    # 비즈니스 계정인지
    is_business = models.BooleanField(default=False)
    
    # 계정별 등급
    grade = models.CharField(max_length=10, default='C')
    