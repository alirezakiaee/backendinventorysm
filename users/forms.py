from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','first_name','last_name')
        error_class = {'first_name': 'form-control is-invalid', 'last_name': 'form-control is-invalid', 'email': 'form-control is-invalid'}
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('email','first_name','last_name')
        error_class = {'first_name': 'form-control is-invalid', 'last_name': 'form-control is-invalid', 'email': 'form-control is-invalid'}