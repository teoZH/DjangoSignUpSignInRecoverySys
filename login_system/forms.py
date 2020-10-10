from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, \
    PasswordChangeForm, SetPasswordForm
from django.contrib.auth import password_validation
from login_system.models import RegisterUser
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username:',
        strip=False,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'id': 'username',
            'placeholder': 'ex. crazy12',
            'autocomplete': 'off',
        }),
        required=True
    )

    password = forms.CharField(
        label='Password:',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'id': 'pass',
            'placeholder': 'Enter your password here',
            'autocomplete': 'off'
        }),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=150,
                                min_length=3,
                                label='Password:',
                                help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(attrs={
                                    'id': 'pass',
                                    'name': 'pass',
                                    'placeholder': 'Enter your password here!'
                                }))

    password2 = forms.CharField(max_length=150,
                                min_length=3,
                                help_text="Enter the same password as before, for verification.",
                                label='Password Confirmation:',
                                widget=forms.PasswordInput(attrs={
                                    'id': 'pass_confirm',
                                    'name': 'pass_confirm',
                                    'placeholder': 'Repeat your password here!'
                                }))

    class Meta:
        model = RegisterUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'autocomplete': 'off',
                'id': 'username',
                'name': 'username',
                'placeholder': 'ex. crazy12'
            }),

            'email': forms.EmailInput(attrs={
                'autocomplete': 'off',
                'id': 'enter_email',
                'name': 'enter_email',
                'placeholder': 'abv@abv.bg'
            })
        }

        labels = {
            'username': 'Username:',
            'email': 'Please enter a valid email!'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=150,
                                   min_length=3,
                                   label='Old password:',
                                   widget=forms.PasswordInput(attrs={
                                       'id': 'old_pass',
                                       'name': 'old_pass',
                                       'autocomplete': 'off',
                                       'autofocus': True,
                                       'placeholder': 'Enter your password here'
                                   }),
                                   strip=False)

    new_password1 = forms.CharField(max_length=150,
                                    min_length=3,
                                    label='New password',
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'new_pass',
                                        'name': 'new_pass',
                                        'autocomplete': 'off',
                                        'placeholder': 'Enter your new password here!'
                                    }),
                                    strip=False,
                                    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(max_length=150,
                                    min_length=3,
                                    label='New password confirmation:',
                                    strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'new_pass_confirm',
                                        'name': 'new_pass_confirm',
                                        'placeholder': 'Repeat your new password!',
                                        'autocomplete': 'off'
                                    }))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254,
                             label='Please enter a valid email!',
                             widget=forms.EmailInput(attrs={
                                 'id': 'enter_email',
                                 'name': 'enter_email',
                                 'placeholder': 'test@example.com',
                                 'autocomplete': 'off'
                             }))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=150,
                                    min_length=3,
                                    label='New password',
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'new_pass',
                                        'name': 'new_pass',
                                        'autocomplete': 'off',
                                        'placeholder': 'Enter your new password here!'
                                    }),
                                    strip=False,
                                    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(max_length=150,
                                    min_length=3,
                                    label='New password confirmation:',
                                    strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'new_pass_confirm',
                                        'name': 'new_pass_confirm',
                                        'placeholder': 'Repeat your new password!',
                                        'autocomplete': 'off'
                                    }))
