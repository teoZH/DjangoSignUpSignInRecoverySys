from django.contrib import admin
from django.contrib.auth.models import User
from login_system.models import RegisterUser

admin.site.register(RegisterUser)
admin.site.register(User)
