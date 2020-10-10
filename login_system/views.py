from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect
from django.db import IntegrityError
from login_system.forms import LoginForm, RegistrationForm, CustomPasswordChangeForm,CustomPasswordResetForm, CustomSetPasswordForm
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from login_system.models import RegisterUser
from django.utils.encoding import force_bytes
from django.core.exceptions import ObjectDoesNotExist



def homepage(request):
    if not request.user.is_authenticated:
        return redirect('login_in')
    return render(request, 'homepage/homepage.html')


def register(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login_in')
            except IntegrityError:
                form = RegistrationForm()
                context = {
                    'form': form,
                    'error': 'Email or username already used!'
                }
                return render(request, 'register/registration.html', context)
    else:
        form = RegistrationForm()
    context = {'form': form, 'error': error}
    return render(request, 'register/registration.html', context)


def login_in(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            error = 'Wrong credentials. Try again!'
    else:
        form = LoginForm()
    return render(request, 'login/login_page.html', {'form': form, 'error': error})


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login_in')
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('homepage')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'password/password_change.html', {'form': form})


def password_reset(request):
    context = {}
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            try:
                user = RegisterUser.objects.get(email=request.POST['email'])
                to_email = request.POST['email']
                from_email = 'admin@example.com'
                context = {
                    'protocol': 'http',
                    'domain': 'localhost:8000',
                    'token': default_token_generator.make_token(user),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'email': user.email
                }
                form.send_mail('password/subject.txt', 'password/reset_instructions.txt', context, from_email, to_email)
                return HttpResponse('Congrats! A mail has been sent to you!')
            except ObjectDoesNotExist:
                return HttpResponse('Congrats! A mail has been sent to you!')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password/password_reset.html', {'form': form})


def password_set(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        user_pk = int(urlsafe_base64_decode(kwargs['uidb64']))
        user = RegisterUser.objects.get(pk=user_pk)
        form = CustomSetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_in')
    else:
        form = CustomSetPasswordForm(request.user)
    return render(request, 'password/pass_change_forgotten.html', {'form': form})


def testing(request):
    context = {}
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            try:
                user = RegisterUser.objects.get(email=request.POST['email'])
                to_email = request.POST['email']
                from_email = 'admin@example.com'
                context = {
                    'protocol': 'http',
                    'domain': 'localhost:8000',
                    'token': default_token_generator.make_token(user),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'email': user.email
                }
                form.send_mail('password/subject.txt', 'password/reset_instructions.txt', context, from_email, to_email)
                return HttpResponse('Congrats! A mail has been sent to you!')
            except ObjectDoesNotExist:
                return HttpResponse('Congrats! A mail has been sent to you!')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'testing/testing.html', {'form': form})

