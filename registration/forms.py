# para el css del fromulario

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
# <========================== para heredar  ========================>
from django.contrib.auth.forms import AuthenticationForm
# <==========================  ========================>
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # super(LoginForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='input-field'),
            Field('password', css_class='input-field'),
            Submit('submit', 'Ingresar', css_class='btn btn-green')
        )
