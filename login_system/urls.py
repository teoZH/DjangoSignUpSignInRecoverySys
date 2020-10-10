from django.urls import path
from login_system import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_in, name='login_in'),
    path('test/', views.testing, name='testing'),
    path('password_change/', views.change_password, name='pass_change'),
    path('password_reset/', views.password_reset, name='pass_reset'),
    path('set_new_password/<uidb64>/<token>/', views.password_set, name='new_pass_set')
]