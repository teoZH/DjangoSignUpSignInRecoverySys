from django.db import models
from django.contrib.auth.models import AbstractUser


class RegisterUser(AbstractUser):
    username = models.CharField('Username', max_length=150, unique=True,help_text= 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.' ,blank=True)
    email = models.EmailField('Email Address', max_length=150, unique=True, blank=True)