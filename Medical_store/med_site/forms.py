import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Username(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^(?=.*\d)(?=.*[@#$%^&+=])(?=.*[a-zA-Z]).{8,}$', username):
            raise ValidationError("Username must contain 8 letters, one number, and one symbol.")
        return username

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
